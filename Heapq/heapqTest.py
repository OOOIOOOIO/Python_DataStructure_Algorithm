# 힙 정렬 알고리즘 --> 정렬된 트리구조
"""
Heap이란 자식노드가 부모노드와 정관계를 가진 트리구조(우선순위 큐를 응용하여 만들 수 있음)

이진 힙의 경우 array나 list와를 사용해 표현할 수 있다.(인덱스를 이용해서 표시할 수 있다)
이때 수식은 n(인덱스)을 부모로 하는 자식 노드의 위치 수식은 (2n + 1)   (2n + 2)가 된다.

Heap은 최대 힙(max-heap : 부모가 자식보다 크거나 같다.),
최소 힙(min-heap : 부모가 자식보다 작거나 같다.)이 있다.

파이썬의 heapq모듈은 최소힙(min-heap)으로 구현되어 있는 모듈이다.

리스트의 길이가 긴 경우에는 시간이 오래걸린다.(리스트를 트리구조로 만들어주고 다시 정렬을 하기 때문)
"""

import heapq

# 힙 생성 : heapq.heapqpush() --> 빈 리스트에 힙 구조로 하나씩 넣기 (add 느낌)
# 힙 생성 : heapq.heapify() --> 기존 리스트를 힙 구조로 만들어주기
# heapq.heappop() --> 가장 작은 데이터 리턴 및 삭제(정렬하지 않아도 min 값을 찾아서 리턴함)
from showHeap import show_tree # showHeap파일에서 show_tree 함수 불러옴
from heapqData import data # heapqDAta파일에서 data 라는 리스트 불러옴


heapq.heapify(data) # 기존 리스트를 힙 구조로 만들어주기(min heap)
print(data)
print(data[0])
print()
print("최댓값 1개 출력 : ", heapq.nlargest(1, data)) # 가장 큰 수 1개 출력 --> 최댓값
print("최솟값 3개 출력 : ", heapq.nsmallest(3, data)) # 가장 작은 수 3개 출력 -> 최솟값
print()
"""
인강 파일이 없음 heap 못 들.
"""

print("heappop() 전 : ", data)
print("데이터 꺼내기 --> ", heapq.heappop(data)) # 제일 작은 원소를 꺼내서 삭제
print("heappop() 후 : ", data)
print()
