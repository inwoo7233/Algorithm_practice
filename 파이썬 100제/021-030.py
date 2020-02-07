# 21 : 2, dictionary를 생성한다.
# 다음 중 set을 만드는 방법이 아닌 것?
#
# 1)  x = {1, 2, 3, 5, 6, 7}
# 2)  x = {}
# 3)  x = set('python')
# 4)  x = set(range(5))
# 5)  x = set()

# 22 : 2
# 다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?
#
# 1)  i / 6 == 0
# 2)  i % 6 == 0
# 3)  i & 6 == 0
# 4)  i | 6 == 0
# 5)  i // 6 == 0

# 23 : X
# print(10/2)의 출력 결과는 5이다.

# 24
name = input("이름을 입력하세요: ")
print(name.upper())

# 25
def solution(n):
	return n * n * 3.14
print(solution(int(input("반지름을 입력하세요: "))))

# 26
planets = {"수성":"Mercury", "금성":"Venus", "지구":"Earth", "화성":"Mars", "목성":"Jupiter", "토성":"Saturn", "천왕성":"Uranus", "해왕성":"Neptune"}
planet = input("한글로 행성이름을 입력해주세요: ")
print(planets[planet])

# 27 : 점수를 int화 해주어야 하고, map과 zip을 쓰면 좀 더 효율적인 코드를 적을 수 있다.
name = input("학생들의 이름을 입력해주세요: ").split()
score = map(int, input("학생들의 점수를 입력해주세요: ").split())
result = dict(zip(name,score))
print(result)

# 28
data = input("문자열을 입력하세요: ")
for i in range(len(data) - 1):
    print(data[i] + data[i+1])

# 29
data = input("알파벳을 입력하세요: ")
if data.isupper():
    print("YES")
else:
    print("NO")
data = input("문자열을 입력하세요: ")
answer = ""
for i in range(len(data)):
    if data[i].isupper():
        answer += data[i]
print(answer)

# 30 : find와 index의 차이. find는 존재하지 않으면 -1을 출력하지만 index는 오류를 발생시킨다.
data = input("대상 문자를 입력하세요: ")
wnt_find = input("찾을 문자를 입력하세요: ")
print(data.find(wnt_find))
print(data.index(wnt_find))
