def add(first, second) :
    sum = first + second
    return sum

def multiply(first, second=1) :
    multiply = first * second
    return (multiply, first, second)

# dictionary <파이썬에서 object로 인식(fuction이 아닌 class로 인식됨)>
# person1 은 class로 생각하면 됨
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}