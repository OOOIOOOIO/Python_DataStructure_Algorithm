import queue

# queue.Queue() --> 큐 생성 / FIFO 방식
# queue.LifoQueue() --> 큐 생성 / LIFO 방식(Stack)
# queue.put(값) --> 값 넣기
# queue.get() --> 값 빼기


q = queue.Queue() # 큐 생성

for i in range(3) :
    print(i)
    q.put(i) # 큐에 넣기

print("일반적인 큐 : ", end = "" )
while not q.empty() :
    print(q.get(), end = " ")

print()
print()

lq = queue.LifoQueue()

for i in range(5) :
    lq.put(i)
print("LIFO 큐(스택) : ", end = "" )
while not lq.empty() :
    print(lq.get(), end = " ")
