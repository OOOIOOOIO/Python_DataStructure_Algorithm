# 언팩킹(unpacking)

pa = (1, 2) # 팩킹

a, b = pa # 언팩킹
print(a, b) # a -> 1, b -> 2
print()
li_data = ["김성호", 23, "인천", (1998, 1, 11)]
"""
name, age, local, birthday = li_data
year, month, day = birthday

print(name, age, local, birthday)
print()

print(year)
print()

"""
str = "Hello" # 문자열 언팩킹

a, b, c, d, e = str
print(a, b, c, d, e)
print()

#=========================================================

# 특정 값을 무시("_")하거나 *를 이용하여 여러개를 언팩킹하기
#name, _, local, _ = li_data # "_"을 통해 무시하기
name, *_ = li_data # *_ 로 여러개 무시할 수 있다 
print(name) # age, birthday are not defined
print()

person_info = ("김성호", "polite159@gmail.com", "010-0000-0000", "032-000-0000")

name, email, *phoneNum = person_info

print(name, email, phoneNum)
print(type(phoneNum)) # * 리스트로 받음
print()

pointValue = [10, 5, 12, 11, 22, 14, 12, 15, 10, 15, 14, 25]

*prePoint, curPoint = pointValue
print(prePoint, curPoint)
print()

address = [("우편번호", 234, 123), ("지역", "서울"), ("지역", "인천"), ("우편번호", 345, 546)]

def show_zipcode(num1, num2) :
    print("우편번호", num1, num2)

def show_local(str) :
    print("지역", str)

for key, *arg in address :
    if key == "우편번호" :
        show_zipcode(*arg) # 알아서 언팩킹 됨
    elif key == "지역" :
        show_local(*arg)
print()

str2 = "김성호/24/1212122211/87989-81314915/인천"

name, age, *id, local = str2.split("/")
print(name)
print(id)
