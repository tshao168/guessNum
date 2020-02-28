import random
r = random.randint (1, 10)
while True :
	num = input ('請輸入任意數字: ')
	num = int (num)
	if r == num :
		print ('很棒! 猜對了')
		break
	elif r > num 	:
		print ('比答案小哦,再試試')
	else :
		print ('比答案大哦,再試試')
