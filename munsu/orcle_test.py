import cx_Oracle
import pandas as pd

# Oracle 연결
conn = cx_Oracle.connect("아이디/비밀번호@호스트:포트/SID")
cursor = conn.cursor()

# 쿼리 실행
query = "SELECT title FROM news"
df = pd.read_sql(query, conn)

cursor.close()
conn.close()
