# 딕셔너리에서 최소값 / 최대값 / 정렬

fruits = {
    "사과" : 300,
    "오렌지" : 200,
    "바나나" : 500,
    "배" : 1000,
    "포도" : 2000
}
# 가격에 따른 최소값과 최대값
# zip() 함수를 이용해서 key와 value를 뒤집는다.

max_fruits = max(zip(fruits.values(), fruits.keys())) # 최대값
print(max_fruits)

min_fruits = min(zip(fruits.values(), fruits.keys()))
print(min_fruits)

sorted_fruits = sorted(zip(fruits.values(), fruits.keys()))
print(sorted_fruits)

fruits_name = zip(fruits.values(), fruits.keys())
print(max(fruits_name)) # zip()은 선언 후 한번만 사용 가능
#print(min(fruits_name)) # 에러 남

# 키 값으로 비교하기
print(min(fruits)) # 키 값으로 비교
print(min(fruits.keys()))
print()
print()

# zip()을 사용하지 않고 key와 value를 보여주기

print(min(fruits, key = lambda n : fruits[n])) # value 값을 기준으로 key 출력 (min에 key 함수를 적용한 예)

print(max(fruits, key = lambda n : fruits[n])) # value 값을 기준으로 key 출력

max_val = fruits[max(fruits, key = lambda n : fruits[n])] # value 값 출력하기
print(max_val)
print()

fruits1 = {"사과 " : 300, "사고" : 300}

print(min(zip(fruits1.values(), fruits1.keys()))) # value가 동일 할 경우에는 키를 가지고 비교를 한다.
