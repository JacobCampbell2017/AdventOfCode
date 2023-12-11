
numbers =  {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

def combineFirstLastNum(string: str) -> int:
    first, last = 0, 0
    
    for char in string:
        if char.isdigit():
            if first == 0:
                first = int(char)
            last = int(char)
    
    numString = str(first) + str(last)
    return int(numString)


def main():
    
    result = 0
    with open('input.txt', 'r') as f:
        for line in f:
            result += combineFirstLastNum(line)
    print(result)

if __name__ == "__main__":
    main()