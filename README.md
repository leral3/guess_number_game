랜덤으로 숫자를 생성한 후에 추측한 숫자를 입력하면, 큰지 작은지 판단해서 알려주고, 다시 추측하는 간단한 게임을 만들어 보겠습니다.


1. 숫자 입력받기 


2. 판단 하기 
테스트를 위해서, 정답은 임의의 숫자로 고정하고, 정답인지 아닌지 판단해보겠습니다. 
여기서 중요한게 있는데, input으로 숫자를 입력 받으면 이 값의 타입은 문자열로 저장됩니다. 
그래서 number = 35 하고 input으로 35를 입력해도 오답입니다. 라고 나옵니다. 
그래서 input으로 받은 숫자를 정수형으로 바꿔줘야합니다. 