import numpy as np
import copy
import random

class Greedy:
    def __init__(self, FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment):
        self.FacilityNum = FacilityNum
        self.CustomerNum = CustomerNum
        self.OpeningCost = np.asarray(OpeningCost)
        self.Demand = np.asarray(Demand)
        self.Assignment = np.asarray(Assignment)
        self.CapacityRest = np.asarray(Capacity)
        self.CustomerChoice = np.zeros((CustomerNum,), dtype=np.int)
        self.choice = np.dtype([('cost', 'i2'), ('j', 'i1'), ('i', 'i2')])
        self.pri = np.zeros([CustomerNum, FacilityNum], dtype=self.choice)
        self.FacilityUsers = np.zeros((FacilityNum,), dtype=np.int)
        self.Cost = 0

    def add(self, CapacityID, CustomerID):
        if self.CapacityRest[CapacityID] >= self.Demand[CustomerID]:
            self.CapacityRest[CapacityID] -= self.Demand[CustomerID]
            self.Cost += self.Assignment[CapacityID][CustomerID]
            if self.FacilityUsers[CapacityID] == 0:
                self.Cost += self.OpeningCost[CapacityID]
            self.FacilityUsers[CapacityID] += 1
            self.CustomerChoice[CustomerID] = CapacityID
            return True
        else:
            return False


    def start(self):
        self.inipri()
        for i in range(self.CustomerNum):
            for choice in self.pri[i]:
                if self.add(choice['j'], choice['i']):
                    break
        Str = "Result: " + str(self.Cost) + '\n' + "Status of facilities: "
        for f in self.FacilityUsers:
            if f == 0:
                Str += '0 '
            else:
                Str += '1 '
        Str += "\nThe assignment of customers to facilities: "
        for c in self.CustomerChoice:
            Str += str(c) + ' '
        Str += '\n'
        return Str

    def inipri(self):
        for j in range(self.FacilityNum):
            for i in range(self.CustomerNum):
                cost = self.Assignment[j][i]
                self.pri[i][j] = (cost, j, i)
        self.pri = np.sort(self.pri, order='cost')
