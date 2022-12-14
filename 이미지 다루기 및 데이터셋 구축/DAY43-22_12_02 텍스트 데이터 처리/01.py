import sklearn
from sklearn.preprocessing import *
import numpy as np
from numpy import *



def normalization(data):
    data_mm = (data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    return data_mm


def numpy_standardization(data):
    """
    
    (각 데이터 - 평균(각 열)) / 표준편차 (각 열)
    """
    std_data = (data - np.mean(data, axis=0))
    return std_data



def main():
    data = np.random.randint(30, size=(6, 5))
    print(data)
    std_data_temp = numpy_standardization(data)
    print(std_data_temp)
    
    no_data = normalization(data)
    print(no_data)
    
if __name__ == '__main__': ##  __name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라. 즉, 내장변수인 name에 main이 들어가면
    main()


