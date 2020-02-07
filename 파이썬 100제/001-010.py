# 1
nums = [100,200,300,400,500]
nums.pop()
nums.pop()
print(nums)

# 2
l = [200, 100, 300]
l.insert(2, 10000)
print(l)

# 3
l = [100, 200, 300]
print(type(l))

# 4 : 3, string
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은?
# 1)  입력 : a =1,   출력 : class 'int'
# 2)  입력 : a = 2.22,   출력 : class 'float'
# 3)  입력 : a = 'p',   출력 : class 'char'
# 4)  입력 : a = [1, 2, 3],   출력 : class 'list'

# 5
a = 10
b = 2
for i in range(1, 5, 2):
    a += i
print(a+b)

# 6 : 2
# 다음은 파이썬 문법 중에서 False로 취급하는 것들 입니다.
# 앗, False로 취급하지 않는 것이 하나 있네요! True를 찾아주세요.
# 1)  None
# 2)  1
# 3)  ""
# 4)  0
# 5)  bool(0)

# 7 : 4,5
# 다음 중 변수명으로 사용할 수 없는 것 2개를 고르시오.
# 1)  age
# 2)  a
# 3)  as
# 4)  _age
# 5)  1age

# 8
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight'])

# 9
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'
print(year, month, day, sep = '/', end = ' ')
print(hour, minute, second, sep = ':')

# 10
n = int(input())
for i in range(1,n+1):
	print(" "*(n-i)+("*"*(2*i-1)))
