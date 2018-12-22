for i in range(1, 72):
    with open(r'Result/p' + str(i) + ".txt", 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        temp = 0
        max = float('inf')
        for j in range(30):
            result = data[j].split()[1]
            if int(result) < max:
                temp = j
                max = int(result)
        print(data[temp], end='\n\n ')
