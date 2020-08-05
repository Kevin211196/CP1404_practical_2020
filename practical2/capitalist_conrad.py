"""
Capitalist Conrad wants us to write a stock-price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is a 50% chance it increases by 0 to 10%,
 and a 50% chance that it decreases by 0 to 5%.If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901).
"""
import random
MAX_INCREASE = 0.1
MAX_DECREASE =0.05

MAX_PRICE =1000
MIN_PRICE=0.01
STARTING_PRICE=10

def main():
    day = 1
    price = STARTING_PRICE
    print("On day {} price is: ${:,.2f}".format(day, price))
    out_file=open('price.txt', 'w')
    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0

        if random.randint(2, 3) == 2:

            price_change = random.uniform(0, MAX_INCREASE)  # uniform return a random float number
        else:
            # generate a random floating-point number
            # between negative MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)
        day += 1
        price *= (1 + price_change)
        out_file.write("On day {} price is:${:,.2f}\n".format(day, price))
        print("On day {} price is:${:,.2f}".format(day, price))

    out_file.close()

if __name__ == '__main__':
    main()