import random
def coupon(x):
	num = '0123456789'
	coupon_no = ''
	for i in range(0, x):
		x = random.randint(0, len(num) -1)
		coupon_no += num[x: x + 1]  #added one by one number till the the value of x is satidfied
	return coupon_no

print(coupon(6))