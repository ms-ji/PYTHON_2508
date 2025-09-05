from datetime import datetime

now = datetime.now()
print(f'datetime.now():{now}')
#2025-08-06 09:41:15.087517

print(now.year) #2025
print(now.month) #8
print(now.day) #6
print(now.hour) #9
print(now.minute) #42
print(now.time()) #09:42:57.083574

#날짜 포맷팅
formatting_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatting_date) #2025-08-06 09:44:59