first = 3
second = 4

# 자바의 if-else if-else
# if (first < second) {
#     print('less first')
#  } else {
#     print('greater second')
#  }

#  기본 if-elif-else
if (first < second) :
    print('less first')
elif (first == second) :
    print('equal')
else :
    print('greater second')

# break
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for fruit in thislist:
    pass
    if (fruit == 'orange') :
        break
    print(fruit)