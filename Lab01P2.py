#Lab01_Problem 2

#PURPOSE
#Find if a user can purchase a house based on house cost and income
#SIGNATURE
#Home_buy : : int, int, int => float
#EXAMPLES
#homw_buy(550000, 25000, 75000)
def downpayment_msg(price, salary, savings_percent):
    DOWNPAYMENT_RATE = 0.25
    downpayment = calc_downpayment(price, DOWNPAYMENT_RATE)
    monthly_saved = calc_monthly_savings(salary, savings_percent)
    months_to_save = calc_months_to_save(downpayment, monthly_saved)
    years = int(months_to_save // MONTHS)
    months = int(months_to_save % MONTHS)
    
    return "If you decided to save ${:0.2f} per month, ".format(monthly_saved) \
            + "it will take you {} years and {} months ".format(years, months) \
            + "to save enough for the downpayment on this home."


# PURPOSE
# Calculate downpayment amount given the house price and the 
# downpayment rate.
# SIGNATURE
# calc_downpayment :: Float, Float => Float
# EXAMPLES
# calc_downpayment(100000, 0.25) => 25000.0
# calc_downpayment(500000, 0.1) => 50000.0
def calc_downpayment(price, downpayment_rate):
    return price * downpayment_rate


# PURPOSE
# Calculate amount saved each month based on the annual salary plus percent of
# salary saved every month.
# SIGNATURE
# calc_monthly_savings :: Float, Float => Float
# EXAMPLES
# calc_monthly_savings(100000, 0.05) => 416.67
# calc_monthly_savings(230000, 0.1) => 1916.67
def calc_monthly_savings(salary, savings_percent):
    return salary * savings_percent / MONTHS


# PURPOSE
# Calculates the number of months it will take to save up the given amount
# based on the amount saved each month.
# SIGNATURE
# calc_months_to_save :: Float, Float => Integer
# EXAMPLES
# calc_months_to_save(25000, 5000) => 5
# calc_months_to_save(300000, 1000) => 100
def calc_months_to_save(amount, monthly_save):
    return amount // monthly_save + (amount % monthly_save > 0)


def main():
    print(downpayment_msg(100000, 50000, 0.25))


main()
