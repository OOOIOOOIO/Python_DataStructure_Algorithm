# pprint(pretty printer) : 자료구조를 보기 좋게 출력해주는 모듈

data = [(1, {"a" : "가", "b" : "나", "c" : "다", "d" : "라"}),
        (2, {"e" : "마", "f" : "바", "g" : "사", "h" : "아"})
        ]

# pprint 모듈에 pprint() 함수를 이용하여 자료구조를 출력해보기

print("일반 print 사용 :", data)

from pprint import pprint

pprint(data)
print()

# arry :  시퀀스 자료구조를 정의하는, list와 차이점은 모든 자료형이 동일해야한다.

import array

str = "abcdefgh"

arr = array.array("u", str) # 선언법 : array("타입코드", 값)
print(arr)

print(array.typecodes) # array 타입코드들 보는 법
print()

arr1 = array.array("i", range(5)) # 선언
print(arr1)

arr1.extend(range(5))
print(arr1)
print(arr1[3:6])
print("0번째 인덱스 : ", arr1[0])
print()

print(list(enumerate(arr1)))
