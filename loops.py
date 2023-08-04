thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for item in items:          // items는 list여야 함
#     pass
for fruit in thislist:
    print(fruit)
pass


#  자바의 for문
#  for(int i=2; i < 10; i++){
#       print(i)
#   }
range(2, 10)
# python의 for 문
for i in range(2,10):
    print(i)


# while
first = 3
while (first < 6) :
    pass
    print('while count {}'.format(first))
    first = first + 1


# list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)

# enumerate의 원리 이해 : enumerate를 만들고 next를 해주면 순서적으로 값이 나온다
# enumerate를 하면 앞은 index, 뒤는 value. 나온 값의 듀플 형태.
# next(fruits_enumerate)
# (0, 'apple')
# next(fruits_enumerate)
# (1, 'banana')
# next(fruits_enumerate)
# (2, 'cherry')
# next(fruits_enumerate)
# (3, 'orange')
# next(fruits_enumerate)
# (4, 'kiwi')
# next(fruits_enumerate)
# (5, 'melon')
# next(fruits_enumerate)
# (6, 'mango')
# next(fruits_enumerate)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# StopIteration

# list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)

# 듀플 묶음
for index_fruit in fruits_enumerate :
    print(index_fruit)

# 듀플 분리
fruits_enumerate = enumerate(fruits)
fruit_print_format = "number: {0}, fruit name : {1}"
for (index, fruit) in fruits_enumerate :
    print(fruit_print_format.format(index, fruit))
    pass

pass