# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 23:54:52 2025

@author: JecheolMoon
"""

x=11

print(f"x={x}") #print시 값을 띄어쓰기 없이 표시하는 방법 f"x={x}" 변수값이 가운데 들어가야 함

if x>10:
    print("x는 10보다 크다")
elif x==10:
    print("x는 10이다")
else:
    print("x는 10보다 작다")
    
# 파이썬 연산자 정리

# 산술연산자
# + 덧셈
# - 뺄셈
# * 곱셈
# / 나눗셈 (실수 결과)
# // 몫 (정수 나눗셈)
# % 나머지 -> 5%2=1 (나누고 나머지이기 때문에)
# ** 지수 승

# 비교 연산자 (True or false)
# == 같다, 3==3 -> True
# != 다르다, 3!=2 -> True
# > 크다
# < 작다
# >= 크거나 같다
# <= 작거나 같다

x=10
y=11
z=12
print(f"x={x}",f"y={y}",f"z={z}",sep="  ") # sep=""은 안에 뭐를 넣으면 그게 반영됨

print("안녕하세요", end="!")  # 안녕하세요!
print("반가워요")            # 이어서 출력됨

for i in range(3):
    print(i)
    