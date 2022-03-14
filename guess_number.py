import random

number = random.randint(1,999)                # 정답을 랜덤으로 생성하기 
print(number)

def number_hint():
    print("랜덤으로 생성된 숫자에 대한 힌트는 총 2가지입니다. 힌트를 확인하시려면 1번 또는 2번을 눌러주세요")

    a = int(input(""))
    if a == 1:
        if number % 2 == 0:
            print("해당 숫자는 짝수 입니다.")
        else:
            print("해당 숫자는 홀수 입니다.")
    
    elif a == 2:
        print("각 자리수를 더한 값은 {} 입니다".format(sum(map(int,str(number)))))

    elif a == 3:
        print("에휴...")

chance = 0

while True:
    try:        
        guess = int(input("숫자를 입력하세요:"))   # input으로 입력받은 숫자의 데이터 타입은 문자열이므로 이를 정수형으로 변환해야함    
        if guess == number:
            print("정답입니다.")
            break                                 # 정답이면, 루프 문을 빠져 나갑니다.          
        elif guess > number:                      # 정답이 아니면 입력한 값의 크기를 판단합니다.
            print("입력하신 값이 더 큽니다.")
        elif guess < number:
            print("입력하신 값이 더 작습니다.")
        
        hint = 0
        if hint == int(input("힌트를 알고 싶으시면 0번을 누르세요")) :
            number_hint()

        if chance == 3:
            print("모든 기회를 다 사용하셨어요 정답은 {} 입니다.".format(number))
            break
        chance += 1
        
    except:
        print("1~999 사이의 숫자를 입력하세요")