from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print "The max possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Invalid guess! You can't guess higher than the max!!!"
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total value: %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Well in lad! You win!"
    else:
      print "Unlucky fella..."

roll_dice(6)
