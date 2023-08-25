# modules.py의 fuction을 사용할 수 있게 하기 위한 방법
import modules #import를 한다는 것은 fuction의 모든 것을 가져오는 것이 아니라 fuction을 인식하는 것 뿐이다.

result_sum = modules.add(8, 1)
pass

# alias (짧게 쓰기 위해서, 위으 방식보다 이 방식을 권장)
import modules as mdls
result_sum = mdls.multiply(8, 1)
pass

# modules 내에 fuction만 있는 것이 아니라 object와 같은 다른 것이 함께 있을 때
# 특정한 class나 object를 사용할 때 내부로 한 번 더 들어가줘야 함.
# 이럴 때 from을 사용
from modules import person1 as ps
print(ps['country'])
pass