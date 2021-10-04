# 딕셔너리 키를 여러 값에 맵핑하기 (collections.defaultdict)

# 일반 딕셔너리
d = {}

d.setdefault("sel", []).append("02") # .setdefault("키", 디폴트값) --> 리스트여서 append() 사용
d.setdefault("sel", []).append("서울")

print(d)
print()

c = {"as" : [i for i in range(5)]}

print(c)
print()

# collections.defaultdict

from collections import defaultdict

d = defaultdict(list) # list로 바로 초기화

d['sel'].append("032") # d["키"] --> 리스트로 초기화 했으니 append() 사용
d['sel'].append("인천")

print(d)
print()

d = defaultdict(set)

d['seoul'].add("02")
d['seoul'].add("서울")

print(d)
print()

# 튜플일 떄

color = [('blue', 3), ('yellow', 2), ('red', 1), ('blue', 4), ('yellow', 5)]

d = defaultdict(list)

for key, value in color :
    d[key].append(value)

li = list(d.items())

print(li)

# 일반 딕셔너리 경우
d2 = {}
for key, value in color :
    d2.setdefault(key, []).append(value)

li2 = list(d2.items())
print(li2)


# 문자열의 문자 개수 세는 법 
str = "hello hi goodmorning"

d = defaultdict(int) # int : key의 개수를 value에 반환

for key in str :
    d[key] += 1

li = list(d.items())

print(li)
