import random
start = input ('請輸入起始值: ')
end = input ('請輸入結尾值: ')
start = int(start)
end = int(end)
print ('**** 你輸入的範圍是從', start, '到', end, '****')
r = random.randint (start, end)
count = 0
while True :
	count = count +1 
	print ('第', count,'次')
	num = input ('請輸入的任意數字: ')
	num = int (num)
	while  num < start or num > end :
		print ("你輸入的數字不在你設定的範圍內")
		count = count-1
		break
	if r == num :
		print ('很棒! 猜對了')
		break
	elif r > num  and  num > start and num < end  :
		print ('比答案小哦,再試試')
	
	elif r < num  and  num > start and num < end  :
		print ('比答案大哦,再試試')
