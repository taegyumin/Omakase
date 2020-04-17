# Pingpong Game


## Problem Description

- 수열이 있고, 숫자는 1씩 증가 또는 감소한다.
- 수열은 1부터 시작한다. 즉, a_{1} = 1
- 수열은 증가 방향으로 시작한다. 즉, a_{2} = a_{1}+1 = 1+1 = 2이다.
- 수열의 n번째 수에 대해, 이 수가 7의 배수 (7, 14, 21,...)거나 7이란 숫자를 포함(7, 17, 27,...)하는 경우 수열의 증감 방향이 바뀐다.


다음과 같이 수열은 진행한다. 증감 방향이 바뀌는 지점은 []로 표시하였다.

	1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6 ...

다음의 제약 하에 `pingpong(x)`의 함수를 작성하라.

- For Loop 또는 Array를 쓰지 말 것.
- Assignment를 쓰지 말 것. 즉, 변수 할당을 하지 말 것. (여기서 질문은, 할당의 범위가 어디까지일까? 할당 연산자를 쓰지 않으면 되나요? Stack에 x외의 참조변수가 쌓이면 안 되나요?

- String을 쓰지 말 것.


## Example

### Code
	pingpong(1)
	pingpong(2)
	pingpong(8)
	pingpong(14)
	pingpong(22)
	pingpong(68)
	pingpong(100)
	pingpong(1000)

### Console
	1
	2
	6
	0
	0
	2
	2
	-26


## Strategy
pingpong(8)의 결과값은 6인데, 이는

- 8 -> 7 (-x)
- 7 -> 6 (+x)
- 6 -> 5 (+x)
- ...
- 2 -> 1 (+x)
- x == 1

따라서, 8 = 1(초기값) + 5*x = 1 + 5 = 6


## Code
[code](https://github.com/taegyumin/Omakase/blob/master/eight-percent_pingpong/pingpong.py)

