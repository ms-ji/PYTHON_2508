import cx_Oracle

class OracleConnection:
    def __init__(self,user='scott',password='pcwk',dsn='192.168.100.66:1521/XE'):
        self.user = user
        self.password = password
        self.dsn = dsn
    def connect(self):
        try:
            #DB 연결
            return cx_Oracle.connect(self.user,self.password,self.dsn)
        except cx_Oracle.DatabaseError as e:
            #데이터 베이스 관련 예외 처리
            error = e.args
            print(f'데이터베이스 오류: {error.message}')
        except Exception as e:
            print(f'Exception: {e}')

def main():
    """
    
    """
    conn = OracleConnection()
    print(f'conn: {conn}')

if __name__ == '__main__':
    main()
