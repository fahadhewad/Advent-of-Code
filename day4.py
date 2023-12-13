file_path = "input.txt"

# Open the file and read its contents
with open(file_path, "r") as file:
    big_string = file.read()

input = big_string

arr = input.split('\n')

sum = 0

for card in arr:
    count = 0
    x, y = card.split(':')
    x, y = y.split('|')
    winners = x.strip().split()
    numbers = y.strip().split()
    for number in numbers:
        if number in winners:
            if count == 0:
                count = 1
            else:
                count *= 2
    sum += count
print(sum)