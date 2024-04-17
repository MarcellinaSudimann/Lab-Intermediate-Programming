with open('icecream.txt', 'r') as file:
  for line in file:
    print(line.strip())
salesData = {}

with open('icecream.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(':')
        flavor = parts[0]
        sales = list(map(float, parts[1:]))
        salesData[flavor] = sales

print(salesData)