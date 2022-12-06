import numpy as np
array = np.array([[1,4,34,11], [25,55,90,82]])
print("각 열을 기준으로 정렬 전 \n", array)


array.sort(axis=0)
print("각 열을 기준으로 정렬 \n", array)

# 넘파이를 통해 코테에서도 남들보다 빠르게 사용이 가능.