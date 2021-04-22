from art import logo, vs
from game_data import data
from random import randint
from replit import clear

print (logo)
game_continue = True
score = 0
first = data[randint(0, len(data)-1)]
second = data[randint(0, len(data)-1)]
while second == first:
  second = data[randint(0, len(data)-1)]

def print_all():
  print (f"\nCompare A: {first['name']}, a {first['description']}, from {first['country']}.")
  print (vs)
  print (f"\nCompare B: {second['name']}, a {second['description']}, from {second['country']}.")
  answer = input("Who has more followers? Type 'A' or 'B':").upper()
  return answer
def next_step():
  global first, second, score
  first = second
  second = data[randint(0, len(data)-1)]
  while second == first:
    second = data[randint(0, len(data)-1)]
  score += 1
def compare_followers():
  if  first['follower_count'] > second['follower_count']:
    return "A" 
  else:  
    return "B" 

answer = print_all()

while game_continue:
  if answer != "A" and answer != "B":
    game_continue = False
    clear()
    print (logo, "\n"f"Sorry, that's wrong. Final score: {score}")
    print (answer)
  elif answer == compare_followers():
    next_step()
    clear()
    print (logo, "\n" f"You are right. Current score: {score}")
    answer = print_all()
  else:
    game_continue = False
    clear()
    print (logo, "\n" f"Sorry, that's wrong. Final score: {score}")

