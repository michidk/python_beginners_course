import sys


print('Counting the numbers of beets I can still buy!')

amount = int(sys.argv[1])
beer_costs = 2
print('I have ' + str(amount) + ' Euro and the beers cost ' + str(beer_costs))
beers = amount / beer_costs
print('I can buy ' + str(beers) + ' beers!')
