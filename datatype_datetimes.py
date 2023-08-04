import datetime # package를 import한 것(파이썬에서는 import를 하는 순간 인스턴스를 하지 않아도 바로 사용할 수 있음)

# print today (오늘 날짜 찍기)
today = datetime.datetime.now()
pass

# [debug console]
today
# datetime.datetime(2023, 8, 4, 18, 14, 14, 72590) : 년,월,일,시,분,초,microsecond
type(today)
# <class 'datetime.datetime'>

# 어제 날짜로 값 세팅하기
yesterday = datetime.datetime(2023, 8, 3)
# datetime.datetime(2023, 8, 3, 0, 0)

# refer) https://www.w3schools.com/python/python_datetime.asp