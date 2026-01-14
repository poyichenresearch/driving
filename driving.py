driving = input('drive before?')
if driving != 'yes' and  driving != 'no':
    print('only yes or no are allowed')
    raise SystemExit
age = input('your age?')
age = float(age)

if driving == 'yes':
	if age >= 18:
		print('ok!')
	else:
		print('what!!!')
elif driving == 'no':
	if age >= 18:
		print('try to get it!')
	else:
		print('good, wait few years')
else:
	print('only yes or no are allow')
