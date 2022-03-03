
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd /home/pi/google_assistant_vietnamese_speaking/src
```
1.2. Edit config bằng lệnh 

```sh
sudo nano create_config.py
```
1.3. Tạo file config sau khi Edit xong bằng lệnh 

```sh
python3 create_config.py
```
1.4. Chạy file 

```sh
python3 start.py
```


Kết quả thành công
```sh
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
INFO:root:Connecting to embeddedassistant.googleapis.com
INFO:root:Using device model inbound-theory-xxxxx-xxxxx-xxxxx and device id xxxxx-xxxxx-xxxx-xxxx-xxxxxxxx
```
1.5. Ra lệnh bằng từ khóa

Sau khi có kết quả thành công, ra lệnh bằng từ khóa "OK Google" hoặc "Hey Google" sẽ có tiếng Ting và bắt đầu chờ lệnh


### STEP2.  Chạy tự động khi khởi động Pi

2.1. Chạy bằng Systemd

2.1.1. Tạo file google.service bằng lệnh

```sh
sudo nano /etc/systemd/system/google.service
```
Tại cửa sổ Nano, gõ dòng lệnh sau

```sh
[Unit]
Description=google
After=alsa-state.service

[Service]
ExecStart = /usr/bin/python3.9  /home/pi/google_assistant_vietnamese_speaking/src/start.py
WorkingDirectory=/home/pi/google_assistant_vietnamese_speaking/src/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```
Bấm Ctrl + X, Y, Enter

2.1.2. Gõ lệnh sau

```sh
sudo systemctl enable google.service
```
Hệ thống sẽ hiện ra
```sh
Created symlink /etc/systemd/system/multi-user.target.wants/google.service → /etc/systemd/system/google.service.
```
Hệ thống đã sẵn sàng tự động chạy tự động Google

2.1.3. Gõ lệnh sau để chạy tự động Google
```sh
sudo systemctl start google
```
hoặc
```sh
sudo reboot
```
2.1.4. Gõ lệnh sau để xem log
```sh
 sudo journalctl -u google.service -f
```
2.1.5. Gõ lệnh sau để stop chạy tự động 

Gõ lệnh để stop tạm thời

```sh
sudo systemctl stop google.service
```
Google sẽ stop không chạy cho đến khi khởi động lại

Gõ lệnh để disable

```sh
sudo systemctl disable google.service
```

Hệ thống sẽ hiện ra
```sh
Removed /etc/systemd/system/multi-user.target.wants/google.service
```
Hệ thống đã stop google không chạy tự động nữa


2.2. Tự động bằng crontab

2.2.1. Tạo nơi lưu log

```sh
cd ~
mkdir logs
```
2.2.2. Khai báo crontab

```sh
crontab -e
```
Chọn 1 để edit bằng nano 
Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi gõ

```sh
@reboot sh /home/pi/google_assistant_vietnamese_speaking/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

2.2.3. Khởi động lại Pi 

```sh
sudo reboot
```
Google Assistant sẽ tự động chạy khi khởi động Pi

2.2.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
2.2.5. Gỡ tự động chạy khi khởi động Pi (Nếu cần)

```sh
crontab -e
```
Chọn 1 để edit bằng nano 

Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi xóa dòng sau

```sh
@reboot sh /home/pi/google_assistant_vietnamese_speaking/src/start.sh >/home/pi/logs/cronlog 2>&1i
```
Bấm Ctrl + X, Y, Enter

Khởi động lại Pi 

```sh
sudo reboot
```
Google Assistant sẽ không tự động chạy khi khởi động Pi nữa

