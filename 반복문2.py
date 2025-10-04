"""
k = int(input("구분: 1 , 주간 2, 야간?"))
m = int(input("대상: 1 , 대인 2, 소인?"))

if k ==1:


    if m == 1:
        pay=50000
    else:
        pay =40000

else:

    if m ==1:

        pay=30000
    else:
        pay=20000

print(f"당신의 입장료 는 {pay}원 입니다.")


#for 반복문

fruit = ["apple" , "grape" , orange , banana"]
#print(fruit[2])

count = 0
for f in fruit:
    print(f)
    count = count +1
    print(count)
print(fruit)

n = [0,1,2,3,4]
for i in n:
    print("hello")
"""

food = ("치킨", "피자", "햄버거", "칼국수")
print(type(food))
for f in food:
    print(f)


number = [273, 103, 5, 32, 65, 9, 72, 880, 99, 50]
for n in number:
    if n & 2 == 0:
        print(n, "는 짝수입니다")
else:
    print(n, "는 홀수 입니다.")

for n in number:
    print("{} 는 {}자리수 입니다".format(n, len(str(n))))


score_list = [98, 58, 65, 78, 44]

i = 0

sum_score = 0
for score in score_list:
    sum_score += score
    sum_score = sum_score + score

    i = i + i

    if score >= 60:
        print(f"(i) 번 학생은 {score} 으로 합격입니다.")
    else:
        print(f"(i)번 학생은 {score} 으로 불합격 입니다")

print(f"총점은 {sum_score}입니다.")
