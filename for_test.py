
"""
#제어문 - 선택문
#복습 주사위 게임 random
import random

a = random.randint(1 ,6) #첫번째 주사위
b = random.randint(1 ,6) #두번째 주사위


print("a값." , a)
print("b값." , b)

if a%2==1 and b%2 ==1:#a,b 모두 홀수이면 (a의 제곱 + b ) 출력하시오
    print(pow(a,2) + b)
elif a%2 ==0 and b%2 ==0:# a,b 모두 짝수이면 절대 값 (a-b)를 출력하시오#abs ()
    print(abs(a-b))#그외 에는 2* (a+b) 를 출력하시오
else:
    print(2+(a+b))
    
#if   a,b 모두 홀수이면 (a의 제곱 +b) 출력하시오
#ellif   a,b 모두 짝수이면  절대값(a-b)를 출력하시오
#else   그외에는 2*(a+b) 를 출력하세요

#제어문 - 반복문 for  whlie

#1. 문자열 이용한 반복문

hi = "안녕하세요"
for ch in hi:
    print("안녕")
    print(ch)

hi = "안녕하세요"
for ch in hi:
    print(ch,end= " ")


korea = "사랑하는 우리나라 대한민국"
count = 0
for i in korea:
    count=count+1
    print(count)



#문자열을 한출로 출력하는데 공백을 만나면 다음줄로 출력하기
korea = "나는 인평자도차고등학교 AI 소프웨어과 1학년 1반 11번 이현서 입니다."
for i in korea:
    print(i,end= " ")
    if i==" ":
        print()
import turtle

#팔각형만들기
for t in range(8):
    turtle.forward(100)
    turtle.left(45)

 i in range(0,501,5): #3의 배수 출력
    print(i,end = "/")



import turtle

#다각형그리기
n = int(input("몇 각형 그릴거야"))
for t in range(n):
        turtle.forward(100)
        turtle.left(360/n)


for i in range(0,501,5): #3의 배수 출력
    print(i,end = "/")


#for문을 이용하여 23부터40까지 출력하시오

for i in range(23,41):
    print(i,end = " ")
"""
#for 문을 이용하여 97 부터77 까지 출력하시오

for i in range(97,76, -1):
    print(i,end = " ")




































