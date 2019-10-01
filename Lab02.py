#Lab02
# 1. Ask at least three questions.
# 2. Each question must have at least two possible answers.
# 3. After the user has answered all the questions, you tell them the result of the quiz.

#PURPOSE
#Design a quiz with conditional answers
#SIGNATURE
#quiz : : int, int, int => float
#EXAMPLES
# Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts
# A
# CORRECT!
def main():

print("Time for a Quiz! Get prepared. And... NO GOOGLE!")
# Question 1
    Q1 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q1 == "A":
        quest1 = "Correct!"
    else:
        quest1 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"
# Question 2
    Q2 = input("What is Seattles Famous landmark? A. UW B. Columbia Tower C. Space Needle")
    if Q1 == "C":
        quest2 = "Correct!"
    else:
        quest2 = "Incorrect! Google it!"   
# Question 3
    Q3 = input("Where is NEU in California located? A. Los Angeles B. Oakland C. Silicon Valley")
    if Q1 == "C":
        quest3 = "Correct!"
    else:
        quest3 = "Incorrect! Look it up on NEU.edu!"   
# Question 4
    Q4 = input("Where in Seattle is the best neighborhood? A. Capitol Hill B. West Seattle C. Lower Queen Anne")
    if Q4 == "C":
        quest4 = "Correct!"
    else:
        quest4 = "Incorrect! Lower Queen Anne is the best!"
# Question 5
    Q5 = input("Where can you eat the best pie? A. McDonalds B. At UPS C. Serious Pie in SLU")
    if Q1 == "C":
        quest5 = "Correct!"
    else:
        quest5 = "Incorrect! Visit Serious Pie in SLU!!"
        
print("Thank you for taking this quiz! Your Results are:")
print("Question 1:", quest1)
print("Question 2:", quest2)
print("Question 3:", quest3)
print("Question 4:", quest4)
print("Question 5:", quest5)
print("Better Luck Next Time!")

main()
