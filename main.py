# generate a number between first argument and second argument
# input from user
# check that input is a number 1 to 10
# check if number is the right guess. otherwise ask again
import sys
from random import randint
start = int(sys.argv[1])
end = int(sys.argv[2])
answer = randint(start, end)
while True:
    try:
        guess = input(f'guess a number {start} to {end}: ')
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print('correct')
                break
            elif int(guess) > answer:
                print('too high')
                continue
            elif int(guess) < answer:
                print('too low')
                continue
    except ValueError:
        print('please enter a valid number')
        continue
