# 사용자에게 문자열 입력 받기
text = input("문자 입력: ")

# 결과를 저장할 빈 리스트 만들기
result = []

# text 안에 있는 문자 하나씩 꺼내기
for c in text:
    # c(문자)를 ASCII 숫자로 변환해서 리스트에 추가
    result.append(ord(c))

# 최종 결과 출력
print("ASCII 변환:", result)
