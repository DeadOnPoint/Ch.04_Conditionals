'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Welcome to Will's Majestic quiz!!")

score = 0

a = float(input("Question 1: What is 5*5? "))
if a == 25:
    score = score + 1
    print("You are correct")
else:
    score = score
    print("You are incorrect the answer is 25")

print("Question 2: Who is the greatest Jedi of all time? ")
print("A. Revan")
print("B. Yoda")
print("C. Obi-Wan Kenobi")
b = str(input("Who is it? "))
if b.upper() == "A":
    print("*psst! good job! You are correct!")
    score = score + 1
else:
    score = score
    print("You are incorrect the answer is A")

c = str(input("Question 3: Who killed Darth Vader? "))
if c.lower() == "darth sidious":
    score = score + 1
    print("You are correct")
else:
    score = score
    print("You are incorrect, the answer is Darth Sidious")

d = str(input("Question 4: What is Goku's Saiyan name? "))
if d.lower() == "kakarot":
    score = score + 1
    print("You are correct")
else:
    score = score
    print("You are incorrect, the answer is Kakarot")

e = str(input("Question 5: What is the name of Universe 7's God of Destruction? "))
if e.lower() == "beerus":
    score = score + 1
    print("You are correct")
else:
    score = score
    print("You are incorrect, the answer is Beerus")

f = str(input("Question 6: What is the name of Goku's first son? "))
if f.lower() == "gohan":
    score = score + 1
    print("You are correct")
else:
    score = score
    print("You are incorrect, the answer is Gohan")

g = str(input("Question 7: Who is the best UK YouTuber? "))
if g.upper() == "KSI":
    score = score + 1
    print("You are correct, it truly is our fatneek")
else:
    score = score
    print("You are incorrect you disgrace")

score = round((score / 7) * 100)

if score <= 100 or score >= 90:
    print("Your grade is", score, "%, a solid A my friend!")
elif score >= 80:
    print("Your grade is", score, "%, a respectable B pal.")
elif score >= 70:
    print("Your grade is", score, "%, I'm sorry it's a C man.")
elif score >= 60:
    print("Your grade is", score, "%, you really need to learn basic knowledge, you got a D man.")
else:
    print("Your grade is", score, "%, transfer to Johnston, you got an F, get out of my sight.")
print()
print("Thanks for taking my Quiz!")