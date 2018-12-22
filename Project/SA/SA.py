import math
import State
import random
import numpy as np

class SA:
    def __init__(self, FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment):
        self.state = State.State(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment)
        self.T = self.state.Cost / 2
        self.coolrate = 0.001
        self.bestrecode = self.state.Cost
        if self.state.CustomerNum <= 50:
            self.Complex = 1
        elif self.state.CustomerNum <= 100:
            self.Complex = 0.5
        elif self.state.CustomerNum <= 150:
            self.Complex = 0.33
        else:
            self.Complex = 0.25

    def run(self):
        self.outside()
        Str = "Result: " + str(self.state.Cost) + '\n' + "Status of facilities: "
        for open in np.nditer(self.state.FacilityUsers):
            if open == 0:
                # print("0", end=' ')
                Str += ("0 ")
            else:
                # print("1", end=' ')
                Str += ("1 ")
        Str += '\n' + "The assignment of customers to facilities: "
        for customer in np.nditer(self.state.CustomerChoice):
            # print(customer, end=' ')
            Str += str(customer) + ' '
        Str += '\n'
        return Str

    def outside(self):
        while self.T >= 1:
            newcost, newdest, newcstm = self.state.ran()
            P = self.adjust(newcost)
            if self.judge(P):
                self.state.remove(newcstm)
                self.state.add(newdest, newcstm)
            if self.bestrecode > self.state.Cost:
                self.bestrecode = self.state.Cost
            dT = self.T * self.coolrate * self.Complex
            self.T -= dT


    def adjust(self, newcost):
        E = newcost - self.state.Cost
        if E < 0:
            return 1
        else:
            E2 = self.bestrecode - newcost
            temp = (-E)/self.T - (-E2)/self.T
            return math.exp(temp)

    def judge(self, P):
        R = random.random()
        if R < P:
            return True
        else:
            return False