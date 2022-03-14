### ĐÂY LÀ HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER CHO PI ZERO WIRLESS, MODUN 2 MIC HAT, 4 MIC ARRAY HOẶC MIC USB

### STEP0. Cài đặt nhanh (Bỏ qua Step1 đến Step5)
Các bạn không muốn trải nghiệm quá trình cài đặt từ Step1 đến Step5, có thể thực hiện theo các bước sau

0.1. Download bộ Image đã cài đặt sẵn tất cả các bước theo link sau:
```sh
https://www.fshare.vn/file/A7S8F7D2TR52
```
hoặc
```sh
https://drive.google.com/file/d/1kvquheNqf9zwObHwCFxWP_HtK-hPQh48/view?usp=sharing
```
0.2. Sử dụng Win32Img để ghi vào thẻ SD 8GB trở lên

0.3. Khai báo file wpa_supplicant.conf như hướng dẫn tại Bước 1.3.

0.4. Cắm thẻ nhớ vào Pi Zero W và boot lên

0.5. Sử dụng SSH để truy cập từ xa vào Console

0.6. Username và password đăng nhập theo mặc định của raspbian (pi/raspberry)

### STEP2. Config Mig, Speaker, LED

2.1. Cài đặt cho Modun ReSpeaker 2 Mic Hat hoặc ReSpeaker 4-Mic Array for Raspberry Pi (Nếu ko sử dụng thì bỏ qua)

2.1.1. Cài đặt Drive cho Modun

Chạy lần lượt các lệnh sau

```sh
sudo apt-get update -y
```
sau đó 
```sh
sudo apt-get upgrade -y
```
sau đó

```sh
git clone https://github.com/respeaker/seeed-voicecard.git
```
sau đó
```sh
cd seeed-voicecard
```
sau đó
```sh
sudo ./install.sh
```
chờ cài đặt kết thúc

khởi động lại

```sh
sudo reboot

```
Sau khi khởi động lại, đăng nhập lại vào console

sau đó tạo một file rỗng asound.conf tại thư mục /home/pi như sau

```sh
sudo nano /home/pi/.asoundrc
```
Gõ space bar sau đó gõ backspace

Bấm lần lượt Ctrl + X, sau đó Y rồi Enter

2.1.2. Cài đặt âm lượng

Vào alxamixer bằng lệnh

```sh
alsamixer
```
bấm F6 để chọn sound card seed, sau đó bấm F5, dùng phím lên trên bàn phím để kéo hết các giá trị lên Max, phím trái, phải để chọn các giá trị Stereo tại các mục tương ứng

Gõ lệnh sau để lưu lại

```sh
sudo alsactl store
```

2.1.2. Cài đặt nút bấm cho các Modun Mic Hat

```sh
python3 -m pip install rpi.gpio
```
2.2. Cài đặt cho Mic USB và Loa

2.2.1. Thống kê ID của Mic USB và Loa (Chỉ dành cho 1/sử dụng Mic USB Soundcard USB hoặc 2/sử dụng phiên bản Pi có nhiều hơn 1 Sound card hoặc cả 1/ và 2/)

Chạy lệnh sau để biết ID của Mic USB
```sh
arecord -l
```
sau đó chạy lệnh sau để biết ID của Loa

```sh
aplay -l
```
Lưu lại thông tin về card_id và device_id ở mỗi kết quả lệnh

2.2.2. Khai báo cho Mic USB (Nếu ko sử dụng Mic USB thì bỏ qua phần này)

Chạy lệnh sau 
```sh
sudo apt-get install pulseaudio -y
```
sau đó 

```sh
sudo nano /home/pi/.asoundrc
```
Cửa sổ nano hiện lên, paste dòng sau, thay thế <card_id> và <device_id> bằng kết quả đã lưu ví dụ 0:0 hoặc 1:0 hoặc 1:1:

```sh
pcm.!default {
  type asym
  capture.pcm "mic"  
  playback.pcm "speaker"  
}
pcm.mic {
  type plug
  slave {
    pcm "hw:<card_id>,<device_id>"
  }
}
pcm.speaker {
  type plug
  slave {
    pcm "hw:<card_id>,<device_id>"
  }
}
```
Bấm lần lượt Ctrl + X, sau đó Y rồi Enter

2.2.3. Copy file thiết lập cho mọi account (Nếu chỉ dùng Account Pi thì bỏ qua bước này)

Chạy lệnh sau
```sh
sudo cp /home/pi/.asoundrc /etc/asound.conf
```

2.2.4. Fix lỗi Audio không chạy tự động của Mic USB

Chạy lệnh sau

```sh
cd /home/pi/       
git clone https://github.com/shivasiddharth/PulseAudio-System-Wide       
cd ./PulseAudio-System-Wide/      
sudo cp ./pulseaudio.service /etc/systemd/system/pulseaudio.service    
sudo systemctl --system enable pulseaudio.service       
sudo systemctl --system start pulseaudio.service       
sudo cp ./client.conf /etc/pulse/client.conf        
sudo sed -i '/^pulse-access:/ s/$/root,pi/' /etc/group    ```

2.2.5. Reboot lại Pi
Chạy lệnh sau
```sh
sudo reboot
```
2.3. Cài đặt điều khiển Led cho Modun ReSpeaker Mic Array v2.0 hoặc ReSpeaker USB Mic Array (Nếu không dùng thì bỏ qua)

2.3.1. Đưa Account đang dùng (Ví dụ pi) vào group root

Chạy lệnh sau
```sh
sudo usermod -aG root account_name
```
2.5. Test loa và mic

2.5.1. Test loa
Chạy lệnh sau
```sh
speaker-test -t wav -c 2
```
2.5.2. Test Mic
Chạy lệnh sau để ghi âm
```sh
arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
```
Chạy lệnh sau để phát lại
```sh
aplay --format=S16_LE --rate=16000 out.raw
```
2.5.3. Test stream giữa Mic và Loa
```sh
arecord --format=S16_LE --rate=16000 | aplay --format=S16_LE --rate=16000
```
