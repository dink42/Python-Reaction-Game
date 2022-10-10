
print('Hello!')
inp = input('How are you!\n')
print(f'Hope this only make your mood {inp} better.\n', 'follow instructions to calculate.')
inp = int(input('First number then ENTER: '))
op = input('Enter operator: ')
inp2 = int(input('Second number then ENTER: '))

if op == '*':
    print(f'Multiplication and your result: {inp*inp2}')
elif op == '+':
    print(f'Addition and your result: {inp+inp2}')
elif op == '-':
    print(f'Substraction and your result: {inp-inp2}')
else:
    print(f'Division and your result: {inp/inp2}')
