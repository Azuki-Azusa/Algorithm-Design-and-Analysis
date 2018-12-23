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

    # add an customer into a facility
    def add(self, FacilityID, CustomerID):
        if self.CapacityRest[FacilityID] >= self.Demand[CustomerID]:
            self.CapacityRest[FacilityID] -= self.Demand[CustomerID]
            self.Cost += self.Assignment[FacilityID][CustomerID]
            if self.FacilityUsers[FacilityID] == 0:
                self.Cost += self.OpeningCost[FacilityID]
            self.FacilityUsers[FacilityID] += 1
            self.CustomerChoice[CustomerID] = FacilityID
            return True
        else:
            return False

    # call init and run greedy alg
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

    # initialize the array
    def inipri(self):
        for j in range(self.FacilityNum):
            for i in range(self.CustomerNum):
                cost = self.Assignment[j][i]
                self.pri[i][j] = (cost, j, i)
        self.pri = np.sort(self.pri, order='cost')
