target = int(input())

even_sum = 0
for number in range(2, target + 1, 2):
    # accumulate even_sum here
    even_sum += number
print(even_sum)
