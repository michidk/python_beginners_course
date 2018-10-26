import sys


girl = sys.argv[1]
boy = sys.argv[2]
max = int(sys.argv[3])

print('An interesting conversation:')
print(girl + ': Hello ' + boy + '!')
print(boy + ': Hello ' + girl + '!')
print(boy + ': Let me show you how well I can count!')
print(boy + ': 0')
print(boy + ': 1')
print(boy + ': 2')
print(boy + ': ...')
print(girl + ': That\'s not efficient! Let me show you!')

for number in range(0, max):
    print(girl + ': ' + str(number))
