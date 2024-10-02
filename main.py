# Input head comments here ***

# Output the purpose of the program

package_type = input('What subscription package do you have? (green, blue, or purple) ')
package_type = package_type.lower().strip()

while package_type not in ['green', 'blue', 'purple']:
    print('Sorry, invalid package type.')
    package_type = input('What subscription package do you have? (green, blue, or purple) ')
    package_type = package_type.lower().strip()

monthly_price = 0
data_provided = 0
data_used = 0

if package_type == 'green':
    monthly_price = float(49.99)
    data_provided = float(2)
    data_used = float(input('How many GB of data did you use?'))
    if data_used > data_provided:
        monthly_price += float(15*(data_used - data_provided))
        if monthly_price >= 75:
            coupon = input('Do you have a coupon? (y/n)')
            while coupon != 'y' and coupon != 'n':
                print('Sorry, invalid coupon.')
                coupon = input('Do you have a coupon? (y/n)')
            if coupon == 'y':
                monthly_price -= 20
elif package_type == 'blue':
    monthly_price = float(70)
    data_provided = float(4)
    data_used = float(input('How many GB of data did you use?'))
    if data_used > data_provided:
        monthly_price += float(10 * (data_used - data_provided))
else:
    monthly_price = float(99.95)

monthly_price = round(monthly_price, 2)

print(f'Your monthly price is: ${monthly_price}')