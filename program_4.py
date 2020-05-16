cost_price,selling_price = float(input('Enter Cost Price of a product :')), float(input('Enter Selling Price of a product :'))

#calculating profit for a product
profit = selling_price-cost_price
print('Profit from this sell:', profit)

#increased profit by 5%
new_profit = profit+(profit*0.05)

new_selling_price = cost_price+new_profit
print('New selling price:', new_selling_price)
