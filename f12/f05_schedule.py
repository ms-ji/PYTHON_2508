import schedule
import time

# 실행할 함수
def job(name):
    print(f'{name}님 즐거운 금요일, 맛나게 점심')

# 매 1분마다 실행
schedule.every(10).seconds.do(job,'이상무')
# 매일 특정 시간에 실행
schedule.every().day.at('12:19').do(job,'홍길동')

# 루프를 돌리면서 작업 실행 여부 확인
while True:
    schedule.run_pending()
    time.sleep(1) #1초 마다 확인