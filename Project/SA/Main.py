import Read
import SA
import time

def run(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment):
    test = SA.SA(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment)
    time_start = time.time()
    Str = test.run()
    time_end = time.time()
    Str += "Time cost: " + str(time_end - time_start) + 's\n\n'
    return Str


for i in range(1, 2):
    print("Calculating p" + str(i), end=' ')
    FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment = Read.Read(i)
    test = SA.SA(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment)
    Str = ''
    for j in range(30):
        Str += run(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment)
    with open(r'Result/p' + str(i) + '.txt', 'w') as file:
        file.write(Str)
        file.close()

    print("Completed")