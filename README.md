랜덤으로 숫자를 생성한 후에 추측한 숫자를 입력하면, 큰지 작은지 판단해서 알려주고, 다시 추측하는 간단한 게임을 만들어 보겠습니다.


1. 숫자 입력받기 


2. 판단 하기 
테스트를 위해서, 정답은 임의의 숫자로 고정하고, 정답인지 아닌지 판단해보겠습니다. 
여기서 중요한게 있는데, input으로 숫자를 입력 받으면 이 값의 타입은 문자열로 저장됩니다. 
그래서 number = 35 하고 input으로 35를 입력해도 오답입니다. 라고 나옵니다. 
그래서 input으로 받은 숫자를 정수형으로 바꿔줘야합니다. 


3. 반복 하기 
while 문으로 무한루프 문을 만들고, 정답을 맞췄을 때만 break 를 해주면 답을 맞출 때까지 반복됩니다. 


4. 크기 판단해서 up & down 알려주기
if - elif 문을 사용하여 입력값(input)이 큰지 판단하고, else 부분은 나머지 작을 때의 메세지를 입력합니다. 


5. 정답 랜덤으로 생성하기
random.randint(1,999)는 1부터 999사이의 난수를 생성하라는 명령입니다.
random 이라는 모듈을 import 해줘야 합니다. 확인을 위해서 생성된 난수를 출력해 놓고, 테스트를 해보겠습니다. 