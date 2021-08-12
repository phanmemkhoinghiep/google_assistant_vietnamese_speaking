
### STEP1. Theo dõi git

1.1. Theo dõi bằng git Desktop

Cài đặt Git Desktop trên PC và theo dõi git phanmemkhoinghiep/google_assistant_vietnamese_speaking

Nếu có File cập nhật sẽ chuyển sang bước 2

Truy cập vào git phanmemkhoinghiep/google_assistant_vietnamese_speaking 

Nếu phát hiện có file nào vừa cập nhật thì chuyển sang bước 2

### STEP2.  Lấy file vừa cập nhật về

2.1. Backup file

Backup file create_config.py, config.json , các file hotword *.ppn bằng lệnh

```sh
sudo cp /home/pi/google_assistant_vietnamese_speaking/src/config.yaml /home/pi/config.json
sudo cp /home/pi/google_assistant_vietnamese_speaking/src/config.yaml /home/pi/create_config.py
```
và
```sh
sudo cp /home/pi/google_assistant_vietnamese_speaking/src/*.ppn /home/pi/
```
2.2. Xóa thư mục Google Assistant bằng lệnh
```sh
sudo rm -rf /home/pi/google_assistant_vietnamese_speaking
```
2.3. Download file update

2.3.1. Download bằng lệnh git
```sh
git clone https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking.git
```

2.4. Restore file

Restore file config.yaml và các file hotword .ppn bằng lệnh
```sh
sudo cp /home/pi/config.yaml /home/pi/google_assistant_vietnamese_speaking/src/config.json
sudo cp /home/pi/config.yaml /home/pi/google_assistant_vietnamese_speaking/src/create_config.py
```
và
```sh
sudo cp /home/pi/*.ppn /home/pi/google_assistant_vietnamese_speaking/src
```

2.5. Chạy lại ứng dụng 

https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/05_running_guide.md

Chờ Google Assistant chạy lại
