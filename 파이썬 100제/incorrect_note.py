# 4 : 3, string
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은?
# 1)  입력 : a =1,   출력 : class 'int'
# 2)  입력 : a = 2.22,   출력 : class 'float'
# 3)  입력 : a = 'p',   출력 : class 'char'
# 4)  입력 : a = [1, 2, 3],   출력 : class 'list'

# 12 : 객체 생성시 health = 545의 형태로 지정해도 정상적으로 객체가 생성된다.
class Wizard:
    def __init__(self,health,mana,armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def attack(self):
        print("파이어볼")
x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

# 18 : map 함수는 두번째 파라미터 리스트의 각 인자에 첫번째 파라미터함수를 적용해준다.
data = list(map(int, input('숫자 3개를 입력하세요: ').split()))
print(int(sum(data)/3))

# 21 : 2, dictionary를 생성한다.
# 다음 중 set을 만드는 방법이 아닌 것?
#
# 1)  x = {1, 2, 3, 5, 6, 7}
# 2)  x = {}
# 3)  x = set('python')
# 4)  x = set(range(5))
# 5)  x = set()

# 30 : find와 index의 차이. find는 존재하지 않으면 -1을 출력하지만 index는 오류를 발생시킨다.
data = input("대상 문자를 입력하세요: ")
wnt_find = input("찾을 문자를 입력하세요: ")
print(data.find(wnt_find))
print(data.index(wnt_find))

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

# 39 : replace 함수로 쉽게 문자내용 변경가능
n = input()
print(n.replace("q", "e"))

# 41 - 1 : 에라토스테네스의 체
def check_prime2(n):
    if (n == 2 or n == 3 or n == 5 or n ==7):
        print("YES")
    elif (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print("NO")
    else:
        print("YES")
check_prime2(int(input("숫자: ")))

# 50 : 버블정렬
def bubble(n, data):
    for i in range(n - 1): # n-1만큼 반복
        for j in range(n - i - 1): # n-1-i까지만 교체작업진행
            # 제일 큰 수가 있었다면 제일 위로 이미 올라갔을 것이므로, 그는 제외하고 나머지를 정렬하는 것이다.
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")
n = int(input("데이터 개수 입력: "))
data = list(map(int, input("데이터들 입력: ").split()))
bubble(n, data)

# 오답노트
