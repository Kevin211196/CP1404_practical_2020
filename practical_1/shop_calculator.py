items = int(input('Numbers of items: '))
while items < 0:
    print('Invalid number of items')
    items = int(input('Numbers of items: '))

total_price = 0

for i in range(items):
    price = float(input('Price of item {}: '.format(i + 1)))
    total_price += price

if total_price > 100:
    total_price -= total_price * 0.1
    
print('Total price of {} items is: ${:.2f}'.format(items, total_price))