file_path = "input.txt"

# Open the file and read its contents
with open(file_path, "r") as file:
    big_string = file.read()

input = big_string

arr = input.split('\n')

c = {}

for i, card in enumerate(arr):
    if i not in c:
        c[i] = 1
    
    count = 0
    x, y = card.split(':')
    x, y = y.split('|')
    winners = x.strip().split()
    numbers = y.strip().split()
    for number in numbers:
        if number in winners:
            count += 1
    
    for n in range(i + 1, i + count + 1, 1):
        c[n] = c.get(n, 1) + c[i]

print(sum(c.values()))