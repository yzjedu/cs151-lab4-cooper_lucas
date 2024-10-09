# Programmers: Lucas Podowski, Cooper Nazar
# Course:  CS151, Zelalem Yalew
# Due Date: 10/9/2024
# Lab Assignment: 4
# Problem Statement: This program is designed to determine how much a customer owes their mobile phone provider based on their subscription package and amount of data used.
# Data In: Package type, data used, whether the user has a coupon or not
# Data Out: Monthly price
# Credits:

# Output the purpose of the program
print("The purpose of this program is to determine how much a customer owes their mobile phone provider based on their "
      "subscription package and amount of data used.")

# Prompt the user to input their subscription package type
package_type = input('What subscription package do you have? (green, blue, or purple) ')
package_type = package_type.lower().strip()

# Make it so any input other than "green", "blue", or "purple" will not work, and prompt the user to try again
while package_type not in ['green', 'blue', 'purple']:
    print('Sorry, invalid package type.')
    package_type = input('What subscription package do you have? (green, blue, or purple) ')
    package_type = package_type.lower().strip()

# Set monthly price, data provided, and data used to zero
monthly_price = 0
data_provided = 0
data_used = 0

# If the package type is green, set the monthly price and data provided accordingly, and prompt the user to input data used.
# If data used is greater than data provided, increase monthly price by 15 for each extra GB of data used
# If monthly price is greater than or equal to 75, prompt the user to input whether they have a coupon or not
# If the user has a coupon, subtract 20 from monthly price
if package_type == 'green':
    monthly_price = float(49.99)
    data_provided = float(2)
    data_used = float(input('How many GB of data did you use last month? '))
    if data_used > data_provided:
        monthly_price += float(15*(data_used - data_provided))
        if monthly_price >= 75:
            coupon = input('Do you have a coupon? (y/n) ')
            while coupon != 'y' and coupon != 'n':
                print('Sorry, invalid coupon type.')
                coupon = input('Do you have a coupon? (y/n) ')
            if coupon == 'y':
                monthly_price -= 20
# If package type is blue, set the monthly price and data provided accordingly, and prompt the user to input data used.
# If data used is greater than data provided, increase monthly price by 10 for every extra GB of data used
elif package_type == 'blue':
    monthly_price = float(70)
    data_provided = float(4)
    data_used = float(input('How many GB of data did you use? '))
    if data_used > data_provided:
        monthly_price += float(10 * (data_used - data_provided))
# If package type is purple, monthly price is 99.95 with unlimited data
else:
    monthly_price = float(99.95)

# Output the user's monthly price
print(f'Your monthly price is: ${monthly_price:.2f}')