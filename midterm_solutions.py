n = []

for i in range(5):
    n.append(int(input('Enter a number: ')))

for x in n:
    if x % 2 == 0:
        print(x)

x = int(input('Number! '))
count = 0
original = x
while x > 1: # x != 1
    x //= 2
    count += 1
    
print('You can divide', original, 'by 2', count, 'times')