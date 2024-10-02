# Input head comments here ***

# Output the purpose of the program

package_type = input('What subscription package do you have? (green, blue, or purple) ')
package_type = package_type.lower.strip()

while package_type not in ['green', 'blue', 'purple']:
    print('Sorry, invalid package type.')
    package_type = input('What subscription package do you have? (green, blue, or purple) ')
    package_type = lower.strip(package_type)

monthly_price = 0
data_provided = 0
data_used = 0

if package_type == 'green':
    monthly_price = float(49.99)
    data_provided = float(2)
    data_used = float(input('How many GB of data did you use?'))
    coupon = input('Do you have a coupon? (y/n)')
    if data_used > data_provided:
        monthly_price += float(15*(data_used - data_provided))
