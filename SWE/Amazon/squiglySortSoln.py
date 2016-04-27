inputList = [1,2,3,4,5,6,7,8,9]

def switch(i, j, list):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def squiglySort(inputList):
    for i in range(len(inputList)):
        if i % 2 is 1:
            if inputList[i] < inputList[i-1]:
                switch(i-1, i, inputList)
        elif i is not 0:
            if inputList[i] > inputList[i-1]:
                switch(i-1, i, inputList)

squiglySort(inputList)
print(inputList)
