"""
quiz_game.py
This is a simple quiz game that asks the user four questions about computer hardware terms.
The user is prompted to play the game, and if they agree, they are asked four questions.
The user's score is calculated based on the number of correct answers, 
and the final score is displayed as a percentage.
Questions:
1. What does CPU stand for?
2. What does GPU stand for?
3. What does RAM stand for?
4. What does PSU stand for?
The game ends with a thank you message.
"""

print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
SCORE = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    SCORE += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    SCORE += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    SCORE += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    SCORE += 1
else:
    print("Incorrect!")

print("That's " + str((SCORE / 4) * 100) + "% correct!")
