import cx_Oracle

def main():
    """
    
    """
    try:
        conn = None
        cursor = None

        # 데이터 베이스 연결
        conn = cx_Oracle.connect('scott','pcwk','192.168.100.66:1521/XE')
        print(f'conn: {conn}')

        #SQL 실행
        cursor = conn.cursor()
        print(f'cursor: {cursor}')

        sql = 'SELECT * FROM emp'
        print(f'sql: {sql}')

        #cursor 통해 접근
        cursor.execute(sql)

        for row in cursor:
            print(row)


    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f'Oracle 데이터 베이스 오류:{error.message}')
    except Exception as e:
        print(f'Exception: {e}')
    finally:
        # 자원 반납(리소스 해제)
        try:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        except:
            pass # 예외 중첩 방지용




if __name__ == '__main__':
    main()
