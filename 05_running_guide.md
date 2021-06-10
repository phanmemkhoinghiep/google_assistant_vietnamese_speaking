
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd /home/pi/google_assistant_vietnamese_speaking/src
```
1.2. Chạy boot bằng lệnh 

```sh
python3 pushtotalk.so
```

1.3. Kết quả thành công
```sh
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
INFO:root:Connecting to embeddedassistant.googleapis.com
INFO:root:Using device model inbound-theory-xxxxx-xxxxx-xxxxx and device id xxxxx-xxxxx-xxxx-xxxx-xxxxxxxx
```
1.4. Ra lệnh bằng từ khóa

Sau khi có kết quả thành công, ra lệnh bằng từ khóa "OK Google" hoặc "Hey Google" sẽ có tiếng Ting và bắt đầu chờ lệnh


### STEP2.  Chạy tự động khi khởi động Pi

2.1. Chạy bằng Supervisor

Thiết lập tự động chạy bot khi bật nguồn, và tự chạy lại khi lỗi

2.1.1. Cài đặt Supervisor

```sh
sudo apt-get install supervisor -y

```
2.1.2. Edit file config 

```sh
sudo nano /etc/supervisor/conf.d/google_assistant_vietnamese_speaking.conf

```
Tại cửa sổ nano, gõ các dòng sau

```sh
[program:vietbot]
directory=/home/pi/google_assistant_vietnamese_speaking/src
command=/bin/bash -c 'cd /home/pi/google_assistant_vietnamese_speaking/src && python3 pushtotalk.so'
numprocs=1
autostart=true
autorestart=true
user=pi
```
Bấm Ctrl + X, Y, Enter

2.1.3. Update supervisor
```sh
sudo supervisorctl update
```
2.1.4. Khởi động lại Pi 

```sh
sudo reboot
```

Google Assistant sẽ tự động chạy khi khởi động

2.1.5. Stop quá trình tự chạy lại khi lỗi (Nếu cần)

```sh
sudo supervisorctl stop google_assistant_vietnamese_speaking
```

Gỡ Google Assistant ra khỏi tự động chạy khi khởi động

```sh
sudo rm -rf /etc/supervisor/conf.d/google_assistant_vietnamese_speaking.conf 
```
sau đó

```sh
sudo supervisorctl update
```
Chờ sau khi có thông báo update

Khởi động lại

```sh
sudo reboot
```
Google Assistant sẽ không tự chạy lại nữa


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
@reboot sh /home/pi/google_assistant_vietnamese_speaking/src/start.sh >/home/pi/logs/cronlog 2>&1i
```
Bấm Ctrl + X, Y, Enter

2.2.3. Khởi động lại Pi 

```sh
sudo reboot
```
Google Assistant sẽ tự động chạy 

2.2.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
2.2.5. Gỡ tự động

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
Google Assistant sẽ không tự động chạy nữa

