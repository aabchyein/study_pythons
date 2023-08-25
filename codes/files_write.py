# 파일을 만들어서 data 변수 안에 있는 문구를 쓰려고 함.
data = "write somethings"

with open('temp_file.txt', 'w') as fw :
    fw.write(data)

pass
