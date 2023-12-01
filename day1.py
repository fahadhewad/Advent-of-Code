file_path = "input.txt"

# Open the file and read its contents
with open(file_path, "r") as file:
    big_string = file.read()

input = big_string

arr = input.split('\n')
sum = 0
for line in arr:

    stringNums = { #sol found online
    "one": 'o1e',
    "two": 't2o',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9e'
    }

    for key, value in stringNums.items():
        line = line.replace(key, value)
        
    number = []
    for char in line:
        if char.isdigit():
            number.append(char)
    value = ""
    value += str(number[0])
    value += str(number[-1])
    sum += int(value)
print(sum)