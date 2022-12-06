# 주성분을 사용해 특성 줄이기
# 사이킷런 손글씨 데이터를 활용하여 특성 행렬을 표준화 처리 및 주성분 특성 줄이기

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

digits = datasets.load_digits() # 8X8 크기의 손글시 숫자 데이터 로드

# 특성 행렬을 표준화 처리
features = StandardScaler().fit_transform(digits.data)

# 99%의 분산을 유지하도록 PCA클래스 객체 생성
pca = PCA(n_components=0.99, whiten=True) # 이런게 있다 정도만 알고 가기. 딥러닝때 사실 이거 까지 안함. 성능이 더 좋다?라고 말할 수도 없음. 
features_pca = pca.fit_transform(features)
print("원본 특성 개수 : ", features.shape[1])
print("줄어든 특성 개수 : ", features_pca.shape[1])

# # 주성분에 투영된 처음 두 개의 특성을 사용해 산점도 출력
# plt.scatter(features_pca[:, 0], features_pca[:, 1])
# plt.show()

# 화이트닝
pca_nowhiten = PCA(n_components=0.99)
features_nowhiten = pca_nowhiten.fit_transform(features)
plt.scatter(features_nowhiten[:, 0], features_nowhiten[:, 1])
plt.show()

# 특성 행렬을 주성분에 투영하려면 components_ 배열 전치하여 행렬곱을 수행합니다.
# 넘파이 allclose()를 사용하여 features_nowhiten 배열과 동일한지 확인
np.allclose(features_nowhiten, np.dot(features, pca_nowhiten.components_.T))

pca = PCA(whiten=True).fit(features)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.show()


# 넘파이 cumsum()를 사용하여 분산을 누적하여 그래프 출력
# 대략 30개의 주성분으로도 80이상의 분산을 유지
# 표준화하지 않은 원본 데이터 사용
pca.fit(digits.data)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.show()
 # 위에서부터 여기까지 많이 다루는 내용이 아니기 때문에 이런 내용이 있구나 정도만 하고 넘어가기로 하자.