import numpy as np

# # COPY 버전

# array1 = np.arange(0, 10)
# array2 = array1.copy()
# array2[0] = 99
# print(array1)
# print(array2)
# # copy유무에 따른 값의 변화



# # numpy 중복된 원소 제거
# array = np.array([1, 2, 1, 2, 3, 4, 3, 4, 5])
# print("중복 처리 전 >>", array)
# print("중복 처리 후 >> ", np.unique(array))




# np.isin() --> 내가 찾는게 있는지 여부 각 index 위치에 true false
array = np.array([1,2,3,4,5,6,7])

iwantit = np.array([1,2,3,10])

print(np.isin(array, iwantit))

# np.where도 많이 쓰는 편이라고 한다.