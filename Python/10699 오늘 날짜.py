# 1

print("2022-09-21")

# 2

# import datetime as dt
# dt라는 이름으로 datetime 가져오기

from datetime import datetime as dt
# datetime 모듈에서 datetime을 dt라는 이름으로 가져오기

n = dt.now()

print(f"{n.year}-{n.month:02d}-{n.day:02d}")
