# Deque : 양방향 큐(데크)는 컨테이너(앞뒤)에 아이템을 넣거나 뺄 수 있다.

import collections

deq = collections.deque("Hello python") # 객체 생성 및 초기화

print(deq)

print(len(deq))
print(deq[0])
print(deq[-1])

deq.remove('H')
print(deq)
print()

deq.append('k') # 오른쪽에 추가
print(deq)
print()

deq.appendleft('k') # 왼쪽에 추가
print(deq)
print()

deq.extendleft('d') # 왼쪽에 추가
print(deq)
print()

deq1 = collections.deque() # 객체 생성

deq1.extend("가나다라마바사")
print(deq1)
print()

deq1.append("아")
print(deq1)
print()

deq1.extendleft(["하파타"])
print(deq1)
print()



# 아이템 꺼내기

print("오른쪽에서부터 꺼내기")
while True :
    try :
        print(deq1.pop(), end =' ')

    except IndexError :
        break;
print()

"""
print("왼쪽에서부터 꺼내기" )
while True :
    try :
        print(deq1.popleft(), end =' ')

    except IndexError :
        break;
"""
