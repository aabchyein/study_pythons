import datetime # package를 import한 것(파이썬에서는 import를 하는 순간 인스턴스를 하지 않아도 바로 사용할 수 있음)

# print today (오늘 날짜 찍기)
today = datetime.datetime.now()
pass

# [debug console]
today
# datetime.datetime(2023, 8, 4, 18, 14, 14, 72590) : 년,월,일,시,분,초,microsecond
type(today)
# <class 'datetime.datetime'>

# 어느 날짜로 값 세팅하기
someday = datetime.datetime(2023, 8, 3)
# datetime.datetime(2023, 8, 3, 0, 0) : datetime은 연,월,일이 기본이라서 시간은 지정해주지 않아도 됨. 시간은 지정해주지 않으면 0으로 setting

someday - today
# datetime.timedelta(days=-5, seconds=50556, microseconds=627191)
# 50556 / (24 * 60 * 60) : 하루를 초로 나타내고 seconds로 나누면 days랑 동일한 값이 나옴
# 0.5851388888888889

# somedelta = someday - today   : somedelta 변수를 만듦
# type(somedelta)  : somedelta의 type 확인
# <class 'datetime.timedelta'>
# somedelta.days   : days를 가져옴
# -5
pass


# 퀘스트 (23년 5월 8일부터 23.8.7 현재까지 흐른 날짜 계산)
today = datetime.datetime(2023, 8, 7)
someday = datetime.datetime(2023, 5, 8)
somedelta = today - someday
somedelta.days  # 결과 : 91
pass




# 24 * 60 * 60 : 하루를 초로 나타내는 방법
# refer) https://www.w3schools.com/python/python_datetime.asp