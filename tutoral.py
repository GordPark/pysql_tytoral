import psycopg2

# 연결 파라미터 설정
conn_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # 데이터베이스 서버가 로컬에 있을 경우
}

# 데이터베이스 연결 시도
try:
    conn = psycopg2.connect(**conn_params)
    print("데이터베이스에 성공적으로 연결되었습니다.")
except psycopg2.Error as e:
    print("데이터베이스 연결 중 오류가 발생했습니다.")
    print(e)