number = 35

guess = int(input("숫자를 입력하세요:"))   # input으로 입력받은 숫자의 데이터 타입은 문자열이므로 이를 정수형으로 변환해야함

if guess == number:
    print("정답입니다.")
else:
    print("오답입니다.")