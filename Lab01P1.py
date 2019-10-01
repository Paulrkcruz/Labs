#Lab01_Problem 1
#PURPOSE
#Find the price per person to split a restaurant bill evenly
#SIGNATURE
#split_bill : : float, float, int => float
#EXAMPLES
#split_bill(100, .2, 2) => 60
#split_bill(100, .2, 3) => 40
def split_bill(bill_amt, num_people, tip):
	    total = bill_amt + bill_amt * tip
	    split = total / num_people
	    return round(split, 2)
	

def main():
	    amt = float(input("How much was the bill? "))
	    people = int(input("How many people were in your group? "))
	    tip_rate = float(input("How much is each person willing to tip? "))
	    split = split_bill(amt, people, tip_rate)
	    msg = "The bill was ${} plus {}% tip split {} ways. Everyone owes ${:0.2f}"\
	          .format(amt, tip_rate * 100, people, split)
	    print(msg)
	

main()
