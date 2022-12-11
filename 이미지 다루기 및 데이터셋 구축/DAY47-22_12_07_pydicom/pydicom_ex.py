# 의료데이터 처리 방법
import pydicom
import matplotlib.pyplot as plt
import numpy as np
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut

window_center = -600
window_width = 1600

# DiCOM 파일을 읽어오는 함수 -> pydicom.read_file(), pydicom.dcmread() # 둘 중 하나 쓰면 되며, 앞에 있는게 직관적이라 많이 씀.
slice = pydicom.read_file('./ID_0000_AGE_0060_CONTRAST_1_CT.dcm')
# print(slice)

s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image = s*slice.pixel_array + b

# DICOM을 변환해서 읽어야됨. 예제에서는 간단한 것을 보여줌. 변환하는건 기업마다 기술력이라 공개 불가.

plt.subplot(1,3,1)
plt.title('DICOM -> Array')
plt.imshow(image, cmap='gray')
# plt.show()

slice.WindowCenter = window_center
slice.WindowWidth = window_width
image = apply_modality_lut(image, slice) #밝기 조절
image2 = apply_voi_lut(image, slice)
plt.subplot(1,3,2)
plt.title("apply_voi_lut")
plt.imshow(image2, cmap='gray')
# plt.show()

# normalization
## normalization하면 좀 더 선명하게 볼 수 있다(고화질(8k)에서 더욱 두드러짐.)
image3 = np.clip(image, window_center - (window_width/2),
                  window_center + (window_width/2))
plt.subplot(1,3,3)
plt.title("normalization")
plt.imshow(image3, cmap='gray')
plt.show()