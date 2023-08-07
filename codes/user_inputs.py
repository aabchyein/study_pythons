username = input("Enter Name : ")
number = input("Enter Number : ")

# 2개의 변수의 type확인
type(username)
# <class 'str'>
type(number)
# <class 'str'>

# number의 타입(str->int)변환
int(number)
# 10
number = int(number)

# casting : python은 casting할 때 괄호로 전체를 묶어줌
number = int(input("Enter Number : "))
pass