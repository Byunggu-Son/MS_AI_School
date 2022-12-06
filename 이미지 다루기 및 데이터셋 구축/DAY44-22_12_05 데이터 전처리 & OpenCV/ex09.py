# 시간 데이터를 이렇게 변환해서 쓰는 경우는 거의 없다고 함.
# 실습을 위한 것이라고 생각.

import pandas as pd

data = pd.Timestamp('2022-12-05 01:40:00') # dataitem 만듦

data_in_london = data.tz_localize(tz='Europe/London')
print(data_in_london)

data_in_london.tz_convert('Africa/Abidjan')
dates = pd.Series(pd.date_range('2/2/2022', periods=3, freq='M'))
temp = dates.dt.tz_localize('Africa/Abidjan')

print(temp)