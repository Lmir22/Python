#displaying user input of food cost
food_Cost = float(input('The cost of the food: $'))

#assigned numbers to tax rate and sales tax
t_RATE = .18
s_TAX = .07

#calculations for tip and tax
tp = (food_Cost * t_RATE)
tx = (food_Cost * s_TAX)

#display the output for the user's food cost
print('The cost of the food: $%.2f' % food_Cost)
print('The appropriate tip rate: $%.2f' % tp)
print('Sales tax amount: $%.2f' % tx)
print('Overall cost: $%.2f' % (food_Cost + tp + tx))