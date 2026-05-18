import base64

text = input("Base64 입력: ")

try:
    decoded = base64.b64decode(text).decode()
    print("결과:", decoded)
except:
    print("디코딩 실패")