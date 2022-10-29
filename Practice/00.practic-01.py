# 로또 번호 만들기

# random라이브러리 활용
#%% (vscode에서 셀 단위 실행 가능하게 해줌.)
import random
lotto = []

for i in range(6):
    lotto_num = random.randint(1,45)
    lotto.append(lotto_num)

lotto.sort()
print(f'로또 번호는 {lotto}입니다.')
#%%
print('*'*20)
## sample을 활용해 더 간단하게
import random
print(random.sample(range(1,45),6))
print('*'*20)
#%%
# numpy로 만들기

import numpy as np
lotto2 = np.random.choice(range(1, 46), 6, replace=False)
print(lotto2)
# %%
