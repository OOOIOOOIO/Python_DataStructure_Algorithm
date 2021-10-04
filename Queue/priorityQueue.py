# 우선순위 큐 구현하기(우선 순위에 따라 아이템을 정렬)
# 우선순위가 가장 높은 아이템을 팝하는 큐를 의미.
# queue.PriorityQueue 클래스를 이용하여 생성 가능(thread 개념을 학습한 후 사용)
# heapq 모듈을 응용해서 우선순위 큐를 구현한다.

import heapq
import queue

class PriorityQueue() :
    def __init__(self) :
        self._list = []
        self._idx = 0 # 들어온 순서

    def put(self, priority, item) :
        heapq.heappush(self._list, (priority, self._idx, item)) # ( ) 튜플을 넣어줌
        #( ) 튜플끼리 비교할 떄 인덱스끼리(0 -> 1 -> 2) 비교를 함
        # priority에 "-"를 왜 븉여주냐면 heapq는 min heap이기 때문에 작은 값을 리턴
        # 우선순위가 높다는 말이 숫자가 높을 때(1순위 < 4순위)(내림차순으로 정렬 --> 큰 순으로 정렬 )
        # 우선순위가 들어올 때 1이 2보다 작지만 -2은 -1보다 작기 때문에 "-"를 붙여줌

        #일반 우선순위 큐는(오름차순으로 정렬 --> 작은 순으로 정렬)
        self._idx += 1

    def pop(self) :
        return heapq.heappop(self._list)#[-1] # [-1] : 인덱싱을 통해 이름 꺼내오기

class Item() :
    def __init__(self, name) :
        self._name = name

    def __repr__(self) :
        return "Item ({!r})".format(self._name)
        # {} 안에 :, ! 등이 올 수 있다.
        # !r이 오게되면 repr을 호출하겠다는 의미
        # !s는 str을 호출하겠다는 의미
        # !a는 ascii로 변환하겠다는 의미

pQ = PriorityQueue() # 객체 생성

pQ.put(3, Item("이은선"))
pQ.put(1, Item("김성호")) # heap 추가
pQ.put(2, Item("김지호"))
pQ.put(3, Item("김기태"))

print(pQ._list)
print()

print(pQ.pop()) # 값 꺼내기
print()

print(pQ._list)
print()

print(pQ.pop()) # 값 꺼내기
print()
