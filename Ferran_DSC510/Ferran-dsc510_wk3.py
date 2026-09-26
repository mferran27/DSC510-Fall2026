# DSC 510
# Week 3
# If Statements Week 3
# Matt Ferran
# 9/27/26

#Change Control Log:
#Change#:1
#Change(s) Made: added lines 23-35 to include if statements for pricing
 #Date of Change: 8/26/26
 #Author: Matt Ferran
#Change Approved by: Matt Ferran
#Date Moved to Production: 9/26/26



# Prints greeting to client
print('Welcome to Larry and His Cable Guys')

# client is able to insert their employer name
company_name = input('What is your company name?')
# client inserts how much cable they would like to purchase and cost calculation
# clients are able to enter a number for how much they would like
try:
    number_of_feet = float(input('How many feet of cable would you like to purchase?'))
except ValueError:
    print('Please enter a numeric value')
    #pricing updates based on total feet to provide a discount for greater volumes
if number_of_feet <= 100:
    price_per_foot = 0.95
elif number_of_feet <= 250:
    price_per_foot = 0.85
elif number_of_feet <= 500:
    price_per_foot = 0.75
else: price_per_foot = 0.55
total_cost = number_of_feet * price_per_foot
divider = ('-' * 40)
# Receipt details print at once for a complete receipt
print('Below are your transaction details:')
print(divider)
print(company_name)
print(f'Total Cable: {number_of_feet:.2f}ft')
print(f'Cost Per Foot: {price_per_foot:.2f}ft')
print(f'Total Cost: ${total_cost:.2f}')
print(divider)
print('Thank you for shopping with us at Larry and His Cable Guys!!')
print(divider)
















