# Numpy 가장 많이 사용되는 함수
# 1. 원소 정렬
import numpy as np
# def -> 오름 차순 정렬 형태
array = np.array([15, 20, 5, 12, 7])
np.save("./array.npy", array)
array_data = np.load("./array.npy")
array_data.sort()
print("오름 차순 >>", array_data)

# 내림차순 정렬
print("내림 차순>> ", array_data[::-1])
#numpy.flip() , list(reversed(closed)) # reversed는 리스트형태로 만들어서 해야된다. 즉, 내장함수인 flip()을 쓰는게 좋다.