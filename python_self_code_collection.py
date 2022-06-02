# 입출력
from sys import stdin
a = stdin.readline();



# 시간 측정
import time
startTime = time.time()
endTime = time.time()
print(startTime - endTime)



# 특정 키 값을 기준으로 정렬하기
array = [('명지', 10), ('띵지', 20), ('김띵지', 30)] 

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))



# 순열
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result) #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]



# 조합
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]



# 중복 순열
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result) 



# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)



# Counter
## 리스트에 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 카운트
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력 -> 3
print(counter['green']) # 'green'가 등장한 횟수 출력 -> 1
print(dict(counter)) # 사전 자료형으로 반환 -> {'red': 2, 'blue': 3, 'green': 1}


# 최대 공약수
import math

## 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
  return a * b // math.gcd(a, b)

a, b = 21, 14

print(math.gcd(21, 14)) # 최대 공약수 (GCD) 계산 -> 7
print(lcm(21, 14)) # 최소 공배수 (LCM) 계산 -> 42



# 방향 벡터 (간단ver)
n = 5
x, y = 1, 1
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

## 이동 계획 확인
for plans in plans:
    ## 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plans == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    ## 공간 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny



# 리스트 join
alpha = ['a', 'b', 'c'] 
print(''.join(alpha)) ## abc



# isalpha
## 문자로 구성되어 있는지 확인 (숫자, 공백 안 됨)
ex1 = 'A'
print(ex1.isalpha()) ## true



# isdigit
## 숫자인지 확인
ex1 = '123456'
print(ex1.isdigit()) ## true


# isalnum
## 알파벳 또는 숫자인지 확인
ex1 = 'Hello3'
print(ex.isalnum()) ## true



# 문자열 나누기 (split)
Example_String = "Hello This is ddingji"
Split_Str = Example_String.split()
print(Split_Str) ## ['Hello', 'This', 'is', 'ddingji']

# split 횟수 지정 (maxsplit)
Examp = "V1-V2-V3-V4"
x = Examp.split("-", 1)
print(x) ## ['V1', 'V2#V3#V4']



# 특정 키 값을 기준으로 정렬하기 (lambda)
times = [list(map(int, stdin.readline().split())) for i in range(N)]
times = sorted(times, key=lambda times: times[0])
times = sorted(times, key=lambda times: times[1])
## [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9],
##  [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]



# 문자열 계산 (eval())
S = '4+5'
print(eval(S)) ## 9



# replace (문자열 대체하기)
ex1 = '가+나+다+라'
ex1.replace('+', '') ## A를 B로 바꾼다

