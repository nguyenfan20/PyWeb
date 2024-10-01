import sys
import os

# Thêm thư mục gốc của dự án vào PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from . import create_app  # Import hàm create_app

app = create_app()  # Khởi tạo app bằng hàm create_app

if __name__ == "__main__":
    app.run()
