string = "Yojulab !"
len(string)
pass
#<debug console>
# len(string)
# 9
# "ju" in string
# True
# "Not" in string
# False
# "Not" not in string
# True

# refer) https://www.w3schools.com/python/default.asp

string[3]
pass
#slicing 기술
#<debug console>
string[3]
# 'u'
string[3:6]
# 'ula'
string[3:]   
# 'ulab !'
string[:-2]
# 'Yojulab'


age = 36
txt = "My name is John, I am " + str(age)
print(txt)
pass
#format 기술 : format 메소드를 사용하여 문자와 숫자를 함게 출력할 수 있다
#<debug console>
txt_second = "My name is John, I am {}."
txt_second
# 'My name is John, I am {}.'
txt_second.format(age)
# 'My name is John, I am 36.'


# 변수는 세 개인데 값을 넣을 곳은 4개. {} 안에 변수를 순서적으로 쓰러고 한다. 번호를 재사용할 수 있다.
quantity = 3  # index 0번째
itemno = 567  # index 1번째
price = 49.95  # index 2번째
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."
pass
#<debug console>
myorder.format(quantity, itemno, price)
# 'I want 3 pieces of item 567 for 49.95 dollars. I have just 49.95.'