# package == module(python)

# function 기본구조(은폐방식)
# definition 되어있는 이름을 먼저 인식하고 안으로 들어가는게 아니라 fuction 호출로 바로 이동
# 그 다음 fuction_name 내부로 들어가게 됨.
def function_name() :
    pass
    return 0

# function 호출
function_name()
pass

# fuction 활용하기( "평범한" params 이용한 결과값 받기)
def add(first, second) :
    sum = first + second
    return sum


# fuction 호출
# return 값을 사용하려면 변수에 담아주고<할당>
# return 값을 사용하지 않는다면 할당이 필요없음. 호출만 하면 됨
result_sum = add(4, 6)
pass

# fuction 활용하기( set default value with params)
# 두 개의 params에서 값이 안 들어가면 그 값이 default로 들어가게 세팅하기
def minus(first, second=0) :
    result = first - second
    return result
# 호출(param이 2개일 때, 1개일 때)
minus(3, 5) # 결과: 3-5=-2
minus(3) # 결과 3-0=3


# return을 tuple datatype으로!
def multiply(first, second=1) :
    multiply = first * second
    return (multiply, first, second) # [multiply, first, second] = (multiply, first, second)

result_tuple = multiply(3, 4)
multiply, first, second = multiply(4)  # 여러개의 return을 받을 수 있다.(변수가 여러개 return이 된다 -> return되는 datatype이 tuple이다)
# result_multiply, result_first, result_second = multiply(4)  # 변수 3개를 다 맞출 필요 없음
pass

# <debug console>
result_multiply
# (12, 3, 4)
type(result_multiply)
# <class 'tuple'>

# 내부에서 들어오는 변수와 외부에서 들어오는 변수의 이름이 같을 때 구분해주기 위해서
# 내부에서 쓰는 변수 이름 앞에는 _(언더바)를 사용하여 구분 ex) _first