# https://github.com/nikifoth

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('Spider')
    elif i % 3 == 0:
        print('Rat')
    elif i % 5 == 0:
        print('Ghost')
    else:
        print(i)
