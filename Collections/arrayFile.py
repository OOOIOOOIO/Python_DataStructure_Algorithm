# array의 내용을 파일에 쓰거나 읽기

import array
import binascii # 이진형태로 데이터를 읽어오거나 쓸 떄 사용

arr = array.array('i', range(5))
print(arr)

# tofile(파일객체) : 파일객체에 쓰는 함수

f = open("./DataArgorithme/text.txt", "w+b")

arr.tofile(f)
f.flush() # 스트림에 있는 데이터를 파일에 밀어넣고 버퍼에 있는 데이터 지우기

with open("./DataArgorithme/text.txt", "rb") as f1 :
    """
    data = f1.read() # 읽기(포인터가 문장 맨 끝으로 감)
    print(binascii.hexlify(data)) # 바이너리형태로 데이터 값 가져옴

    f1.seek(0) # 포인터(마우스 커서)의 위치를 제일 처음으로 되돌리기

    """
    arr2 = array.array("i")
    arr2.fromfile(f1, len(arr)) # 데이터 값 가져옴
    print(arr2)
