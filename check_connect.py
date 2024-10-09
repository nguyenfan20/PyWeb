from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def check_database_tables():
    username = 'root'
    password = 'admin'
    host = 'localhost'
    port = '3306'
    database = 'tmdt'

    connection_string = f'mysql+pymysql://root:123456@localhost/tmdt?charset=utf8mb4'
    # Tạo engine như trước
    engine = create_engine(connection_string)
    
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES"))
            print("Các bảng trong cơ sở dữ liệu:")
            for table in result:
                print(table[0])  # In tên bảng

    except SQLAlchemyError as e:
        print("Lỗi khi truy vấn:", e)

check_database_tables()

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def check_connection():
    # Thay đổi thông tin kết nối theo cấu hình của bạn
    username = 'your_username'
    password = 'your_password'
    host = 'localhost'
    port = '3306'
    database = 'your_database'

    # Tạo chuỗi kết nối
    connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
    
    try:
        # Tạo engine
        engine = create_engine(connection_string)
        
        # Kết nối và kiểm tra
        with engine.connect() as connection:
            print("Kết nối thành công với MySQL")
            result = connection.execute(text("SELECT VERSION()"))  # Sử dụng text()
            version = result.fetchone()
            print("Phiên bản MySQL:", version[0])

    except SQLAlchemyError as e:
        print("Không thể kết nối với MySQL:", e)

check_connection()
