list_food = ["햅버거","치킨","피자"]
for food in list_food :
    print(food)


print("hello world")


hi = "안녕"
for s in hi:
    print("hi")


world = ["지구","화성","금성","태양","달"]
for world in world:
    print(world)



score_list = [98,54,60,45,84]
number = 1
for score in score_list:
    if score >= 60:
        print("{}학생은 합격 입니다", format(number))  
    else:
        print("{}학생은 불합격 입니다")
        number += 1