# fuction 동작하는지 확인 해보기->웹으로 그대로 가져다 사용하면 됨
# def mlmodel(data:dict) :
#     print('data with dict {}'.format(data))
#     return data # dictionary 형태로 return

# result = mlmodel({'meg':'hellow !'})
# print('result : {}'.format(result))




# with machine learning model
import pickle # 학습시킨 모델을 외부에서도 사용하기 위해 pickle로 저장해서 불러올 수 있게 만든다.

def mlmodelwithregression(data:dict) :
    print('data with dict {}'.format(data))   # {'texture_mean':16.34, 'perimeter_mean':87.21} --> data로 대치됨
    # data dict to 변수 할당
    texture_mean = data['texture_mean']
    perimeter_mean = data['perimeter_mean']
    
    # pkl 파일 존재 확인 코드 필요(★방어코드★)

    result_predict = 0
    # 학습 모델 불러와 예측
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 리턴(dictionary형태로)
    result = {'radius_mean':result_predict[0]}
    return result

# 예제(value) : [[16.34, 87.21]]
# 파라미터 : key, value 형식으로 넣어줌
result = mlmodelwithregression({'texture_mean':16.34, 'perimeter_mean':87.21})
print('result : {}'.format(result))

