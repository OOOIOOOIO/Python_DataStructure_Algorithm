# dequeu 자료구조 응용(양쪽이 뚫려있는 큐 구조)
# deque를 이용해 고정크기 큐를 생성하기(maxen = n)

from collections import deque

# maxlen = n 고정크기 생성
dQ = deque(maxlen = 4)  # 4개의 아이템을 갖는 큐를 생성
dQ.append("aa")
dQ.append('bb')
dQ.append('cc')
dQ.append('dd')

print(dQ)
print()
dQ.append('ee')

print(dQ) # 새로운 아이템 ee가 추가되면서 맨 앞에 있는 aa 아이템은 자동으로 삭제(FIFO)
print()


# =============================================================================
# 파일에 있는 lines에서 find_word를 찾으려고 하는데
# lines에서 한줄씩 가져와 readline으로 넘겨준다
# 만약 찾는 단어가 없다면 문장을 deque에 넘겨준다

def search_word(lines, find_word, history) :
    previous_lines = deque(maxlen = history)
    for readline in lines :
        if find_word in readline :
            yield readline, previous_lines # 제네레이터 발생, readline과 previous_lines 응답을 기다림
        previous_lines.append(readline)


if __name__ == '__main__' : # 이 파일에서만 실행하겠다는 의미(메인함수 느낌), 다른 파일에선 실행 안됨
    with open(r"C:\Users\polit\python_DataArg\Generator\dequeTest.txt", "r", encoding = "UTF-8") as f : # 파일 입력방법

        for fline, prevTexts in search_word(f, "좋은", 8) : # 언팩킹
            for preline in prevTexts :
                print(preline)
                print("제너레이터 호출 된 문장 --> 여기서 작동 멈춤 : ", fline)
                print("=" * 50)

# with open(r"C:\Users\polit\python_DataArg\Generator\dequeTest.txt", "r", encoding = "UTF-8") as f : # 파일 입력방법
#     fword = search_word(f, "좋은", 8) # 제너레이터 생성
#     print(fword)

#     print(next(fword))
#     # for문을 한번 돌면서 처음 "좋은"이 없는 문장들은 previous_lines에 append()해주고
#     # "좋은"을 만나면 작동을 멈추고 yield 값을 리턴함 --> 중요 마치 단계별로 있는 컨티뉴 같은 느낌??

#     print(next(fword))
#     # 다시 호출하게되면 처음 "좋은"은 무시하고 다음 "좋은"이라는 단어를 찾음.
#     # 마찬가지로 "좋은"을 만나면 작동을 멈추고 yield 값을 리턴함(다시 처음으로 돌아감)

#     print(next(fword))
#     # 다시 호출하게 되면 마찬가지로 앞에 있는 "좋은"은 그냥 일반 단어처럼 무시하고
#     # 새로 나오는 "좋은"이라는 단어를 만나면 작동을 딱 멈추고 yield 값을 리턴함(다시 처음으로 돌아감)

#     print()
