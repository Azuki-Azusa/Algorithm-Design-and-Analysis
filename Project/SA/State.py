import numpy as np
import random
class State:
    def __init__(self, FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment):
        self.FacilityNum = FacilityNum
        self.CustomerNum = CustomerNum
        self.OpeningCost = np.asarray(OpeningCost)
        self.Demand = np.asarray(Demand)
        self.Assignment = np.asarray(Assignment)
        self.CapacityRest = np.asarray(Capacity)
        self.CustomerChoice = np.zeros((CustomerNum,), dtype=np.int)
        self.FacilityUsers = np.zeros((FacilityNum,), dtype=np.int)
        self.Cost = 0
        self.start()


    def ran(self):
        cost = float("inf")
        desttemp = cstmtemp = -1
        Range = 10
        for i in range(Range):
            dest = random.randint(0, self.FacilityNum - 1)
            cstm = random.randint(0, self.CustomerNum - 1)
            src = self.CustomerChoice[cstm]
            self.remove(cstm)
            while True:
                if self.add(dest, cstm):
                    if self.Cost < cost:
                        cost = self.Cost
                        desttemp = dest
                        cstmtemp = cstm
                    self.remove(cstm)
                    break
                else:
                    dest = random.randint(0, self.FacilityNum - 1)
            self.add(src, cstm)
        return cost, desttemp, cstmtemp




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

    def remove(self, CustomerID):
        i = CustomerID
        j = self.CustomerChoice[CustomerID]
        self.CapacityRest[j] += self.Demand[i]
        self.Cost -= self.Assignment[j][i]
        self.FacilityUsers[j] -= 1
        self.CustomerChoice[i] = -1
        if self.FacilityUsers[j] == 0:
            self.Cost -= self.OpeningCost[j]

    def start(self):
        i = 0
        j = random.randint(0, self.FacilityNum - 1)
        while i < self.CustomerNum:
            if self.add(j, i):
                i += 1
            j = random.randint(0, self.FacilityNum - 1)