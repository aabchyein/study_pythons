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
# <debug console>
# thislist[1] = 'watermelon'
# thislist[1:3] = ['cherry','watermelon']    : watermelon, cherry의 순서를 바꿀 때 사용(index 1,2번을 바꿀 때)

# sort
# thislist.sort()   : 알파벳 순서대로 정렬됨 -> 0:'apple'  1:'cherry'  2:'kiwi'  3:'mango'...
# thislist.sort(reverse=True)    : 기본은 ASC정렬이지만 reverse=True를 할 경우 DESC

# 붙여넣기(뒤에다 항목을 추가)
thislist = ["apple", "banana", "cherry"]
thislist.append('melon')
# thislist = ['apple', 'banana', 'cherry', 'melon']    : append를 사용해 list 두에 항목을 계속 추가할 수 있음

# 삭제 (값을 지정해서 없애기)
thislist.pop()
# 'orange'     : pop은 뒤에서부터 값을 삭제

# 초기화 방식
thislist = []
thislist = list()
# 다음 자바의 문법과 위의 문법은 같은 문법이다 -> List thislist = new List();
pass