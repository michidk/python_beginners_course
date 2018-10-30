import sys


print('Counting the numbers of beers I can still buy!')
credit = int(sys.argv[1])


def get_amount(money, price):
    result = money / price
    return str(int(result))


print('I can buy:')
print(' - ' + get_amount(credit, 1.5) + ' beers!')
print(' - ' + get_amount(credit, 1.3) + ' spezis!')
print(' - ' + get_amount(credit, 1.7) + ' weissbiers!')
