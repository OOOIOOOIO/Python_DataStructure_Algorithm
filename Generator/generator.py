# 제너레이터(generator / yield)
# yield의 리턴 값이 generator object가 된다.
# yield는 generator를 생성하고 generator next() 함수를 가지고 있다.

# 제너레이터를 사용하는 이유는 작업을 하던 중 중간중간 다른 작업이 필요할 때 호출을 해
# 다른 작업들을 하고 다시 돌아올 수 있기 때문

def generatorEx(n) :
    for i in range(n) :
        yield i ** 2 # 응답을 받고 수행하겠다는 의미

gen = generatorEx(4) # 객체 생성

print(generatorEx(4)) # 객체정보만 출력됨

print(gen) # 마찬가지로 객체 정보만 출력됨

# print(gen.next())
print(next(gen)) # next() 함수를 통해 제너레이터 수행(yield를 만났을 때 수행)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # 에러 발생. 왜냐면 제너레이터(발생기)를 빠져나왔기 때문에
gen = generatorEx(4) # 다시 객체를 생성하고 시작해줘야 다시 동작을 함

print(next(gen))
print()

def countdown(n) :
    while n > 0 :
        yield n
        n -= 1
    print("End")

cnt = countdown(3) # 객체 생성
print(cnt)
print(next(cnt))
print(next(cnt))
print(next(cnt))
# print(next(cnt))
print()

for i in countdown(5) : # for 문은 자동으로 next()를 해준다
    print(i)
