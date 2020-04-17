import sys
sys.setrecursionlimit(10000)
##Python은 재귀함수 최대 depth가 약 1000이므로, 설정을 통해 recursion-limit을 10,000으로 증가시킨다.
##Stack(정적 할당 메모리 공간)에 참조변수들이 쌓일 거니까.


def search_7(x):
    '''
    RETURN  자연수 x에 숫자 7이 포함돼 있으면 True, 그렇지 않으면 False를 반환함.
    '''

    if x % 10 == 7:
        # input x의 일의 자리가 7인지 확인하고, 만약 7이라면 True를 반환함.
        return True

    elif x < 10:
        # x의 일의 자리가 7이 아니면서 10 미만이라면 더 이상 조사해보지 않아도 x는 7을 갖지 않으므로 False를 반환함.
        return False

    else:
        # x의 일의 자리가 7이 아니고, 10 이상이라면 십의 자리, 백의 자리 등을 차례로 조사해봄.
        return search_7(int(x / 10))


def increment(x):
    if x == 1:
        # 종료 시점을 의미함.
        # 임의의 자연수 n에 대해, 수열의 |a_{n+1} - a_{n}|의 값을 결정함.
        # 이 문제에서는 |a_{n+1} - a_{n}| == 1
        return 1
    else:
        if (x % 7 == 0 or search_7(x)):
            # 만약 x가 7의 배수이거나 7을 포함하고 있으면 증분의 방향을 바꿈.
            return - increment(x - 1)
        else:
            # 그렇지 않으면 증분의 방향은 그대로임.
            return + increment(x - 1)


def pingpong(x):
    # x는 문제에서 말하는 수열의 번째수를 의미함.
    if x == 1:
        return 1 #a_{1} == 1임을 의미함.
    else:
        return pingpong(x-1) + increment(x-1)


def get_result(func, arg_list: list) -> list:
    result = []
    for arg in arg_list:
        result.append(func(arg)) #Python에서 함수는 1급 객체 (First-Class)라서 input parameter로 전달 가능.
    return result


x_s = [
    1, 2, 8, 14,
    22, 68, 100, 1000
    ]

result = get_result(pingpong, x_s)
print(result)

from matplotlib import pyplot as plt
import numpy as np

n = 100
x = np.linspace(1, n, n)
y = [pingpong(i) for i in x]
y_max = max(y)
y_min = min(y)

plt.axis([1, n, y_min, y_max])
plt.yticks(list(range(0, y_min, -1)) + (list(range(0, y_max, 1))))
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('pingpong(x)')
plt.title('pingpong problem')

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()