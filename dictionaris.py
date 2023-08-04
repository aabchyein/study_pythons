# 초기화 방법
# empty initial (값이 없을 때 초기화의 2가지 방식)
thisdict= {}
thisdict = dict()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# [debug console]
# len(thisdict) : thisdict의 length확인
# 3
# type(thisdict) : thisdict의 type확인
# <class 'dict'>
# thisdict['model'] : key 인 model의 값을 확인
# 'Mustang'
# thisdict['brand'] = "Yojulab" : thisdict의 key를 선택하고 값을 할당하면 값이 변경됨
# thisdict.keys()
# dict_keys(['brand', 'model', 'year']) : thisdict의 key만 불러올 수 있음
# thisdict.values()
# dict_values(['Yojulab', 'Mustang', 1964]) : thisdict의 value만 불러올 수 있음


# for문
dict_format = "key : {0}, value : {1}"
for key, value in thisdict.items():
    print(dict_format.format(key, value))
    pass
pass

# add item in dict : dict에 값을 추가로 넣는 방법(key를 설정하고 값만 할당하면 됨)
# key 값이 이미 존재하면 값이 변경됨.
thisdict['color'] = 'Red'

# remove item in dict : del을 넣고 key값을 넣어주면 삭제됨
# del thisdict를 할 경우 전체 삭제되므로 주의!
del thisdict['year']


