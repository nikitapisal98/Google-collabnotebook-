import sys
import random
top_of_range = (input("type a num: "))

if top_of_range.isdigit():
  top_of_range=int(top_of_range)


if top_of_range<=0:
  print("type a greater num: ")

random_number=random.randint(0,top_of_range)
guesses=0

while True:
  guesses+=1
  user_guess= input("guess a num: ")
  if user_guess.isdigit():
    user_guess=int(user_guess)
  else:
    print("Try using digit next time")
    continue

  if random_number==user_guess:
    print("Bora! you got it right")
    print(f"The guess is over after only {guesses} tries ;)")
    break
  elif random_number<=user_guess:
    print("you gotta guess low!")
  elif random_number>=user_guess:
    print("Aim high!")
