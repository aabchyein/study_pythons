# slicing (번호 즉, index를 활용함)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# <debug console>
type(thislist) 
# <class 'list'>  : 변수 thislist의 type이 list인 것을 알 수 있음
len(thislist)
# 7  : thislist의 length를 알 수 있음
thislist[1:3]
# ['banana', 'cherry']  : 1,2까지만 나옴
thislist[:-2]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi']
thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']



# change value in list (banana->watermelon)
thislist[1] = 'watermelon'

# <debug console>
# thislist[1:3] = ['cherry','watermelon']    : watermelon, cherry의 순서를 바꿀 때 사용(index 1,2번을 바꿀 때)
# thislist.sort()   : 알파벳 순서대로 정렬됨 -> 0:'apple'  1:'cherry'  2:'kiwi'  3:'mango'...
# thislist.sort(reverse=True)    : 기본은 ASC정렬이지만 reverse=True를 할 경우 DESC
pass