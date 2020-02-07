# 11
s = 0
for i in range(1,101):
    s += i
print(s)

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

# 13
planets = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
num = int(input('몇 번째 행성이 궁금한가요?')) - 1
if num <= len(planets):
    print(planets[num])

# 14
num = int(input('숫자 : '))
if num % 3:
    print(num)
else:
    print('짝')

# 15
name = input('이름이 뭐예요 : ')
print('안녕하세요. 저의 이름은 {}입니다.'.format(name))

# 16 : 문자열도 [::-1]로 거꾸로 받아올 수 있다.
original = input('로꾸거?')
print(original[::-1])

# 17
height = int(input('키가 몇이니? '))
if height >= 150:
    print('넌 통과야')
else:
    print('나가리')

# 18 : map 함수는 두번째 파라미터 리스트의 각 인자에 첫번째 파라미터함수를 적용해준다.
data = list(map(int, input('숫자 3개를 입력하세요: ').split()))
print(int(sum(data)/3))

# 19
data = list(map(int, input('숫자 2개를 입력하세요: ').split()))
print(data[0]**data[1])

# 20
data = list(map(int, input('숫자 2개를 입력하세요: ').split()))
print(data[0]//data[1],data[0]%data[1])

