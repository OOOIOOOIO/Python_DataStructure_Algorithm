# namedtuple : 딕셔너리보다 메모리가 작음

aa = ("홍길동", 24, "남")

print(aa)

bb =("강복녀", 21, "여")

print(bb[0])
print()
for n in [aa, bb] :
    print( "%s는 %d세의 %s성 입니다."%(n))
print()


# 사용법
import collections

Person = collections.namedtuple('Person', 'name age gender')

aa = Person(name = "강길동", age = 25, gender = '남')

bb = Person(name = "강길여", age = 56, gender = "여")

for n in [aa, bb] :
    print("%s는 %d세의 %s성 입니다."%(n))
print()


#=========================================================================

# OrderedDict : 자료의 순서를 기억하는 사전형 객체

dic = {}

dic["a"] = "apple"
dic["b"] = "banana"
dic["c"] = "camera"

for i, j in dic.items() : # 표준 딕셔너리는 순서를 기억하지 않음
    print(i, j)
print()

dic2 = collections.OrderedDict()

dic2["a"] = "apple"
dic2["b"] = "banana"
dic2["c"] = "camera"

for i, j in dic2.items() : # 자료의 순서를 기억
    print(i, j)
print()

print("비교를 이용한 표준 사전과 OrderedDict의 차이점")

dic3 = {}

dic3["a"] = "apple"
dic3["b"] = "banana"
dic3["c"] = "camera"

dic4 = {}

dic4["a"] = "apple"
dic4["c"] = "camera"
dic4["b"] = "banana"

print("표준 딕셔너리 : ",dic3 == dic4) # 순서를 틀리게 선언해도 True가 나옴
print()

dic5 = collections.OrderedDict()

dic5["a"] = "apple"
dic5["b"] = "banana"
dic5["c"] = "camera"

dic6 = collections.OrderedDict()

dic6["a"] = "apple"
dic6["c"] = "camera"
dic6["b"] = "banana"

print("OrderedDict : ",dic5 == dic6) # 순서를 틀리게 선언해도 True가 나옴
print()
