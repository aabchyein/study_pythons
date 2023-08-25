# 1. 파일 존재 확인
import os

file_path = 'codes/temp_file.txt'
if os.path.exists(file_path) : # 존재 여부 return -> True/False -> 그래서 if문 사용
    # 2. 파일 관련 업무 실행 -> (파일을 'r' 즉, 읽을 목적으로 열려고 한다.)
    with open(file_path,'r') as fr:   # 앞(name)에는 파일이름, 뒤(mode)에는 목적을 쓴다
        pass   # 파일을 읽기 전
        load_file_read = fr.read()
        pass   # 파일을 읽은 후 (load_file_read 변수에 temp_file의 내용이 담긴다)
else :
    print('File Not exists!')