import datetime
import time

# 41 : n까지 이르러 반복문을 나온건 그 전까지 걸러지지 않았다는 뜻
def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("YES")
    else:
        print("NO")
check_prime(int(input("숫자: ")))

# 41 - 1 : 에라토스테네스의 체
def check_prime2(n):
    if (n == 2 or n == 3 or n == 5 or n ==7):
        print("YES")
    elif (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print("NO")
    else:
        print("YES")
check_prime2(int(input("숫자: ")))

# 42
m = int(input())
d = int(input())
def findDay(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020,a,b).weekday()]
print(findDay(m,d))

# 43
num = int(input("입력: "))
binary = []
while num > 0:
    binary.append(str(num % 2))
    num = num // 2
binary.reverse()
print(''.join(binary))

# 44
list = list(input("입력: "))
sum = 0
for i in list:
    sum += int(i)
print(sum)

# 45
print(int(time.time() / 60 / 60 / 24 // 365) + 1970)

# 46
sum = 0
for i in range(1,101):
    str_i = str(i)
    for s in str_i:
        sum += int(s)
print(sum)

# 47 : set자료형은 중복을 제거한다.
people = [
         ('이호준', '01050442903'),
         ('이호상', '01051442904'),
         ('이준호', '01050342904'),
         ('이호준', '01050442903'),
         ('이준', '01050412904'),
         ('이호', '01050443904'),
         ('이호준', '01050442903'),
         ]
print(len(set(people)))
for person in people:
    people.remove(person)
    if person not in people:
        people.append(person)
print(len(people))

# 48
alphabet = list(input("알파벳들을 입력하세요: "))
for i in range(len(alphabet)):
    if alphabet[i].isupper():
        alphabet[i] = alphabet[i].lower()
    elif alphabet[i].islower():
        alphabet[i] = alphabet[i].upper()
print(''.join(alphabet))

# 49
numbers = list(map(int,input("숫자를 입력하세요: ").strip().split()))
print(max(numbers))

# 50
def bubble(n, data):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")
n = int(input("데이터 개수 입력: "))
data = list(map(int, input("데이터들 입력: ").split()))
bubble(n, data)