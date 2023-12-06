print("Welcome to My Computer Quiz")

playing = input("Do yo want to play? ").lower()

if playing.lower() != "yes":
    quit()
print("Okay! Let's play")

score = 0
print('Question No. 1')
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

print('Lets Go to Next Question')

print('Question No. 2')
answer = input("What is the square root of 16? ").lower()
if answer == "4":
    print("correct")
    score += 1
else:
    print("incorrect")

print('Lets Go to Next Question')

print('Question No. 3')
answer = input("What is the opposite of hot? ").lower()
if answer == "cold":
    print("correct")
    score += 1
else:
    print("incorrect")

print('Lets Go to Next Question')

print('Question No. 4')
answer = input("What is the opposite of black? ").lower()
if answer == "white":
    print("correct")
    score += 1
else:
    print("incorrect")

print('Lets Go to Next Question')

print('Question No. 5')
answer = input("What is the opposite of big? ").lower()
if answer == "small":
    print("correct")
    score += 1
else:
    print("incorrect")
print("You Got " + str(score) + " questions correct" )
print("You Got " + str((score/5)*100) + "%." )

print("Congratulations :) :) ")
print("You have Compleated the Quiz")