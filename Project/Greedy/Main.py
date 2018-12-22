import Read
import Greedy
import time

Str = ''
for i in range(1, 72):
    Str += 'p' + str(i) + ':\n'
    FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment = Read.Read(i)
    test = Greedy.Greedy(FacilityNum, CustomerNum, Capacity, OpeningCost, Demand, Assignment)
    time_start = time.time()
    Str += test.start()
    time_end = time.time()
    Str += "Time cost: " + str(time_end - time_start) + 's\n\n'

with open(r'Result.txt', 'w') as file:
    file.write(Str)
    file.close()
