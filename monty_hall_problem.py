import random

swapped_correct = 0
non_swap_correct = 0

n = int(input('how many trials? '))
for trials in range(n):
    correct_door = random.randint(1, 3)
    picked_door = random.randint(1, 3)

    if picked_door == correct_door:
        non_swap_correct += 1
        swapped_correct += 0
    else:
        # pick door not correct, so monty hall is going to show us another wrong door,
        # and so we will accident ourselves into the only door left, which is correct
        swapped_correct += 1

print(swapped_correct / n, non_swap_correct / n)
