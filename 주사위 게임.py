"""
import random
a = random.randint(1 ,6)
b = random.randint(1 ,6)

print("a값. " , a)
print("b값. " , b)

if a%2==1 and b%2 ==1:
    print(pow(a,2) + b)
elif a%2 ==0 and b%2 ==0:
    print(abs(a-b))
else:
    print(2+(a+b))


hi = "안녕하세요"
for ch in hi:
    print("안녕")
    print(ch)

hi = "안녕하세요"
for ch in hi:
    print(ch,end= " ")


korea  = "나는 인평자동차고등학교 AI소프웨과 1학년 1반 11번 이현서 입니다"
for i in korea:
    print(i,end= " ")
    if i=="  ":
        print()
        """


