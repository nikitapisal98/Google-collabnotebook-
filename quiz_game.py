import sys
print("Welcome ! to the world of quiz")

playing=input("Are you ready to play?")
if playing.lower() != "yes":
  print("okay,bye!")
  sys.exit()
else:
  print("lets get you started ;)!")

answer = input ("what is the capital of India ? ")
print(f"You entered: {answer}")
if answer.lower().strip() in ['new delhi', 'delhi']:
  print("correct!")
else:
  print("incorrect!")

print("thank you!")
