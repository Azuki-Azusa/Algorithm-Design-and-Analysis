# Get the info in instance
def Read(n):
    with open(r'../Instances/p' + str(n), 'r') as f:
        data = f.read()
        data = data.split()
        FacilityNum = int(data[0])
        CustomerNum = int(data[1])
        Capacity = []
        OpeningCost = []
        Demand = []
        Assignment = []
        for i in range(FacilityNum):
            Capacity.append(int(data[2 + 2 * i]))
            OpeningCost.append(int(data[3 + 2 * i]))
        iter = 2 + 2 * FacilityNum
        for i in range(CustomerNum):
            Demand.append(int(float(data[iter + i])))
        iter += CustomerNum
        for j in range(FacilityNum):
            Assignment.append([])
            for i in range(CustomerNum):
                Assignment[j].append(int(float(data[iter + j * CustomerNum + i])))
        '''
        print(Capacity)
        print(OpeningCost)
        print(Demand)
        print(Assignment)
        '''
        f.close()

        return FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment