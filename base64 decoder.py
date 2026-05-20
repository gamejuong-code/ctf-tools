import base64

print("1. Encode")
print("2. Decode")

choice = input("선택: ")
text = input("문자열 입력: ")

try:
    if choice == "1":
        encoded = base64.b64encode(text.encode()).decode()
        print("인코딩 결과:", encoded)

    elif choice == "2":
        decoded = base64.b64decode(text).decode()
        print("디코딩 결과:", decoded)

    else:
        print("잘못된 선택")

except:
    print("변환 실패")
