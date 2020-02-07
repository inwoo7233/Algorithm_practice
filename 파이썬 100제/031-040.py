# 31 : 3번. O(b-a)의 시간복잡도를 가진다.
# 다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?
#
# 1)  l[i]
# 2)  l.append(5)
# 3)  l[a:b]
# 4)  l.pop()
# 5)  l.clear()

# 32 : strip() -> 조이기
coverLetter = input("입력: ")
words = coverLetter.strip().split()
print(f"출력: {len(words)}")

# 33 : range(start,stop) or range(start,stop,step)
numbers = input("입력: ").split()
print("출력: ", end='')
for num in numbers[::-1]:
    print(num, end=' ')

# 34 : int(i) for i in l로 리스트 내용 한번에 list화 가능
# (map은 하나의 object이기 때문에 출력하기 귀찮음), sorted로 리스트 정렬가능
user_input = input()
l = list(user_input.strip().split())
l = map(int, l)
if l != sorted(l):
    print("NO")
else:
    print("YES")

# 35 : one은 내부적으로는 그저 two함수 자체만 불러온다.
# two는 중첩함수로서 n에 대한 정보는 가지지만, value는 따로 파라미터로 받아야한다.
# 즉, one을 호출하더라도 one이 two를 리턴하기 때문에, 해당 리턴값에 또 파라미터(value)를 전달해주어야 함수가 정상적으로 작동한다.
def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two
a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

# 36
num = int(input('숫자를 입력하세요: '))
for i in range(1,10):
    print(num*i,end=' ')

# 37
data = input('입력: ').strip().split()
max = 0
for i in range(len(data)):
    if data.count(data[i]) > data.count(data[max]) :
        max = i
print(f"{data[max]}(이)가 총 {data.count(data[max])}표로 당선됨")

# 38
data = input('점수입력: ').strip().split()
data.sort()
rank = 0
num = 0
for i in range(len(data) - 1,0,-1):
    if data[i] == data[i-1]:
        num += 1
        continue
    if rank == 3:
        break
    num += 1
    rank += 1
print(num)

# 39 : replace 함수로 쉽게 문자내용 변경가능
n = input()
print(n.replace("q", "e"))

# 40
total = 0
count = 0
limit = int(input())
n = int(input())

for i in range(n):
    if total <= limit:
        total += int(input())
        count = i
print(count)
