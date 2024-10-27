import random

random_num = random.randint(1, 10)

print('You flipped a coin!')

if random_num % 2 == 0:
    print('YOU GOT HEADS')
else:
    print('YOU GOT TAILS')
