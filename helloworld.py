# simple cal 2 para with operator
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……

paraOne = input('Para 1:' )

paraTwo = input('Para 2:' )

operator = input('Operator: ')

print('exec =>>>', paraOne, ' ', operator, paraTwo)

if operator == ('+'):
	print(int(paraOne) + int(paraTwo))
elif operator == ('-'):
	print(int(paraOne) - int(paraTwo))
elif operator == ('*'):
	print(int(paraOne) * int(paraTwo))
elif operator == ('/'):
	print(int(paraOne) / int(paraTwo))
else:
	print('happy new year 2019');


