"""
    [ collection ]

    Counter : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 클래스
            딕셔너리 형태로 반환
"""

import collections

print(collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee'])) # 시퀀스를 이용하는 방법(리스트 사용)
print(collections.Counter({"가" : 3, "나" : 2, "다" : 4})) # 딕셔너리로 밸류값이 큰 순서로 반환
print(collections.Counter(a = 2, b = 4, c = 1)) # 문자열에 숫자를 맵핑하면 리스트형태로 b가 4개 a가 2개 c가 1개라는 의미
print()

container = collections.Counter() # 생성자 선언
print(container)

container.update("aabcdeffgg") # 문자열에 있는 하나하나의 개수 반환
print(container)
print()

container.update({'c' : 2, 'f' : 3}) # f가 3개 추가 c는 2개 추가
print(container)


# Counter 접근하기

for n in "abdfeh" :
    print("%s : %d"%(n, container[n])) # n이 a일 때 a가 몇개인지 알 수 있음
print()

ct = collections.Counter("Hello jenny") # 공백도 포함
ct["x"] = 0
print(ct)
print()

print(list(ct.elements())) # 요소들 출력
print()

# most_common(n) 메소드 사용하기 : 상위 n개를 시퀀스로 만든다

ct2 = collections.Counter()
with open('./DataArgorithme/text.txt', 'rt') as f :
    for li in f :
        ct2.update(li.rstrip().lower()) #rstrip : 왼쪽 공백 제거

# most_common [(a : 4)... (z : 9)] 이런식으로 반환. 그래서 언팩킹을 해줘야됨
print(ct2.most_common())

for item, cnt in ct2.most_common(5) :
    print("%s : %2d"%(item, cnt))
print()


# Counter 객체는 산술 / 집합 연산이 가능하다.

ct3 = collections.Counter(['a', 'b', 'c', 'b', 'd', 'a'])
ct4 = collections.Counter('a aeroplane')

print(ct3)
print(ct4)

print("더하기 :", ct3 + ct4) # 합쳐짐

print("빼기 :", ct3 - ct4) # 빼짐

print("교집합 :", ct3 & ct4) # 교집합

print("합집(union0) :", ct3 | ct4) # 합집합 : 최대값인 경우를 출력
print()

# defaultdict : 생성자(컨테이너)를 초기화(만들) 때 default 값을 지정한다. 

def default_aa() :

    return "aa"

dic = collections.defaultdict(default_aa, n1 = "하이") # n1 -> key, "하이" -> value
print(dic)
print(dic["n1"])
print(dic['n2']) # key값이 없으면 함수가 호출
