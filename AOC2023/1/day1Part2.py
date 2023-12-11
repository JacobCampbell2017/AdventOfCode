numbers =  {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

def combineFirstLastNum2(string: str) -> int:
    first, last = -1, -1
    numberList = []
    index = 0
    for char in string:
        if char.isdigit():
            numberList.append((int(char), index))
        index += 1
    
    for key in numbers:
        indexFound = 0
        totalIndex = 0
        tempString = string
        while key in tempString:
            indexFound = tempString.index(key)
            totalIndex += indexFound + len(key)
            numberList.append((key, totalIndex - len(key)))
            tempString = tempString[indexFound+len(key):]        
                   
    # print(numberList)
    for (x, y) in numberList:
        
        if (first == -1):
            first = y
        if (y < first):
            first = y
        if (last == -1):
            last = y
        if (last < y):
            last = y
            
    # print(first, last)
    for item in numberList:
        if first == item[1]:
            first = item[0]
            break
    
    for item in numberList:
        if last == item[1]:
            last = item[0]
            break
    
    # print(first, last)
    if first in numbers:
        first = numbers[first]
    if last in numbers:
        last = numbers[last]
    
    # print(first, last)
    return int(str(first) + str(last))
    

def main():
    
    result = 0
    with open('input.txt', 'r') as f:
        for line in f:
            result += combineFirstLastNum2(line)
    print(result)

if __name__ == "__main__":
    main()