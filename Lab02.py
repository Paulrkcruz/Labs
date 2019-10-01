#Lab02
# 1. Ask at least three questions.
# 2. Each question must have at least two possible answers.
# 3. After the user has answered all the questions, you tell them the result of the quiz.

#PURPOSE
#Design a quiz with conditional answers
#SIGNATURE
#quiz : : int, int, int => float
#EXAMPLES
#
def main():

# Question 1
    Q1 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q1 == "A":
        quest1 = "Correct!"
    else:
        quest1 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"
# Question 1
    Q2 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q1 == "A":
        quest2 = "Correct!"
    else:
        quest2 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"   
# Question 1
    Q3 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q1 == "A":
        quest3 = "Correct!"
    else:
        quest3 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"   
# Question 1
    Q4 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q4 == "A":
        quest4 = "Correct!"
    else:
        quest4 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"
# Question 1
    Q5 = input("Where in Seattle is the BEST French Bakery? A. Bakery Nuevo B. Flours C. Kurts")
    if Q1 == "A":
        quest5 = "Correct!"
    else:
        quest5 = "Incorrect! Visit Bakery Nuevo in Capitol Hill for the best French Deserts!"
        
print("Thank you for taking this quiz! Your Results are:")
print("Question 1:", quest1)
print("Question 2:", quest2)
print("Question 3:", quest3)
print("Question 4:", quest4)
print("Question 5:", quest5)

main()
