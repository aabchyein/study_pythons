# 퀘스트 
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# user input을 받아 그 값만큼 fruits list의 값을 출력
# 출력은 index, fruit name
# Q 입력하면 while문 종료
# <예시>
# Loops count : 2
# 1 : "apple"
# 2 : "banana"
# Loops count : Q  # 종료

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
number = input("Loops count: ")
fruit_print_format = "{0}: {1}"

while number != "Q" :
    count = int(number)
    if (count == "Q") :
        break
    elif (0 < count <= len(fruits)) :
        for (index, fruit) in enumerate(fruits[:count]) :
            print(fruit_print_format.format(index+1, fruit))
    else :
        print("값을 다시 입력해주세요")
    number = input("Loops count: ")