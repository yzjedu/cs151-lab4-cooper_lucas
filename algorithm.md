# Algorithm Document

1. prompt user to input package type: "What subscription package do you have? (green blue or purple)"
2. make package type lower case and without spaces
3. while package type is not "green" "blue" or "purple"
   1. output: "Wrong package type"
   2. prompt use to input package type: "What subscription package do you have? (green blue or purple)"
   3. make package type lower case and without spaces
4. make empty integers for monthly price, data provided, and data used
5. Check for package types
    1. If package type is 'green'
       1. monthly price is 49.99, data provided is 2
       2. prompt user to input data used as a float: "How many GB of data did you use last month?"
       3. if the data used is greater than the data provided
          1. increase the monthly price by 15*(data used - data provided)
          2. prompt user to input if they have a coupon: "Do you have a coupon? (y/n) "
             1. while the coupon is not 'y' or 'n'
                1. output: 'invalid coupon type'
                2. prompt the user to input if they have a coupon: "Do you have a coupon? (y/n) "
             2. if they have a coupon 
                1. subtract 20 from monthly price 
   2. otherwise if the package type is 'blue'
      1. monthly price is 70, data provided is 4
      2. prompt the user to input data used as a float: "How many GB of data did you use last month? "
      3. if data used is greater than data provided
         1. increase monthly price by 10 *(data used - data provided)
   3. otherwise monthly price is 99.95
6. round monthly price by 2 decimal places
7. output: "Your monthly price is: {monthly price}"