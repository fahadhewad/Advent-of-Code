file_path = "input.txt"

# Open the file and read its contents
with open(file_path, "r") as file:
    big_string = file.read()

input = big_string

arr = input.split('\n')
sum = 0

for line in arr:
    total = {
        'red' : 0,
        'green' : 0,
        'blue' : 0,
    }
    id, line = line.split(':')
    id = id.split()
    id = id[1]
    for sub in line.split(';'):
        d = {
        'red' : 0,
        'green' : 0,
        'blue' : 0,
        }
        for ball in sub.split(','):
            n, colour = ball.split()
            d[colour] = int(n)
        for k in total:
            total[k] = max(total[k], d[k])
    sum += total["red"] * total["blue"] * total["green"]
print(sum)   