# bisect 모듈 : 정렬된 상태로 아이템(데이터)을 추가할 수 있는 모듈
# 데이터가 많은 리스트를 사용할 경우 heap 방식보다 성능이 좋다.(시간과 메모리 낭비를 줄일 수 있다)
# heap은 리스트를 트리로 만들고 다시 정렬을 하기 때문이다.

 # bisect.bisect(리스트, 값) # 인덱스 값 반환
 # bisect.insort(리스트, 값) # 리스트를 정렬 상태로 유지
 # bisect.insort_right(리스트, 값) # 만약 중복이 있다면 뒤에 나온 값이 오른쪽에 배치 ( == .insort(리스트, 값)
 # bisect.insort_left(리스트, 값) # 만약 중복이 있다면 뒤에 나온 값이 왼쪽에 배치 --> bisect.bisect_left랑 같이 써야됨 꼭~!!
import random
import bisect

random.seed(1) #  반복적으로 동일하게 랜덤값이 들어가게 하는 함수 random.seed()
               # 1 자리에 시간값을 주로 넣음

print("random.seed() test : ", end ="")
for i in range(5) :
    print("%5.4f"%(random.random()), end = " ")
print()

print("New Index List")
print("========== =========== ===========")

list = []

for n in range(1, 15) :
    num = random.randint(1, 100) # rnadint --> 1 <= x <= 100 // random --> a <= x < b
    pos = bisect.bisect(list, num)# 아이템이 추가되었을 때 인덱스 값 반환
    bisect.insort(list, num) # 리스트를 정렬 상태로 유지, 만약 중복이 있다면 뒤에 나온 값이 오른쪽에 배치
    print("%3d %3d"%(pos, num), list)
