# while 문
"""
i = 1
sum = 0

while i <=100:
    sum += i
    i +=1
print("1부터 10까지의 합:",sum)

#3부터 15까지 출력하는 while 문 작성

i = 3
while i <= 15:
    print(i)
    i = i +1

#for 문으로 면경

for i in range(3,16):
    print(i)

while True: #무한반복
    jumsu = int(input("점수를 입력하세요: "))
    if jumsu >= 0 and jumsu <=100:
        break
    print("당신의 점수는 ",jumsu,"점 입니다")
"""
fruit = ["사과", "포도", "배", "참외"]

for i in fruit:
    print(i)
# => while 변경 len(fruit)
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
