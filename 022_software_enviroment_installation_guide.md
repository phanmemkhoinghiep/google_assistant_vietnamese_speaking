### ĐÂY LÀ HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER CHO PI ZERO WIRLESS, MODUN 2 MIC HAT, 4 MIC ARRAY HOẶC MIC USB

### STEP1. Cài đặt hệ điều hành Raspbian

1.1. Download Raspberry Pi OS
Tối ưu cho phần cứng Pi Zero Wireless nên Vietbot chỉ cần bản OS Buster Lite tại trang chủ Pi


1.2. Flash vào thẻ nhớ
Sử dụng tool của Raspberry hoặc Etcher

1.3. Config để vào được SSH qua WiFi

1.3.1. Cắm lại thẻ nhớ vào máy

1.3.2. Sử dụng Notepad ++ để tạo file có tên là wpa_supplicant.conf trong thư mục boot của thẻ nhớ với  định dạng file Unix (Edit -> EOL converion -> UNIX/OSX Format là Unix (LF)), nội dung là các tham số tên SSID và mật khẩu tương ứng
Chú ý, tham số country có thể đổi sang us hoặc vn tùy theo cài đặt tại bộ phát WiFi
```sh
country=vn
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="testing"
    psk="testingPassword"
}
```
1.3.3. Tạo file rỗng có tên là SSH trong thư mục boot 

1.4. Truy cập ssh vào Pi Zero Wirless

1.4.1. Cắm thẻ nhớ vào Pi Zero Wireless, chờ Pi boot up xong, xác định IP của Pi từ Modem, Access Pint

1.4.2. Sử dụng putty truy cập ssh vào địa chỉ IP của Pi với username là pi, password là raspberry

### STEP2. Cài đặt các thư viện chung cho Vietbot và thư viện cho Python trên OS

2.1. Cài đặt các thư viện chung cho Vietbot

Chạy lần lượt các lệnh sau
2.1.1.
```sh
sudo apt-get update -y
```
sau đó 
```sh
sudo apt-get upgrade -y
```
2.1.2.

```sh
sudo apt-get install git python3-pip  libportaudio2  libportaudio-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl2-mixer-2.0-0 pulseaudio portaudio19-dev libffi-dev libssl-dev

```
và 

```sh
sudo apt-get install python3-dev
```

2.2. Khởi động lại

```sh
sudo reboot

```

### STEP3. Cài đặt các gói Python

3.1. Nâng cấp PIP

Chạy lần lượt các lệnh sau
```sh
python3 -m pip install --upgrade pip

```
3.2. Cài đặt các gói Python 

```sh

python3 -m pip install mutagen PyAudio  pyalsaaudio pyyaml pyusb  termcolor pixel-ring apa102 pvporcupine rpi_ws281x  
```
và

```sh
python -m pip install --upgrade google-assistant-sdk[samples] --upgrade google-auth-oauthlib[tool] google-assistant-grpc 
```
và

```sh
python3 -m pip install pygame==2.1.0

```

### STEP4. Config Mig, Speaker, LED

4.1. Cài đặt cho Modun ReSpeaker 2 Mic Hat hoặc ReSpeaker 4-Mic Array for Raspberry Pi (Nếu ko sử dụng thì bỏ qua)

4.1.1. Cài đặt Drive cho Modun

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

4.1.2. Cài đặt âm lượng

Vào alxamixer bằng lệnh

```sh
alsamixer
```
bấm F6 để chọn sound card seed, sau đó bấm F5, dùng phím lên trên bàn phím để kéo hết các giá trị lên Max, phím trái, phải để chọn các giá trị Stereo tại các mục tương ứng

Gõ lệnh sau để lưu lại

```sh
sudo alsactl store
```

4.1.2. Cài đặt nút bấm cho các Modun Mic Hat

```sh
python3 -m pip install rpi.gpio
```
4.2. Cài đặt cho Mic USB và Loa

4.2.1. Thống kê ID của Mic USB và Loa (Chỉ dành cho 1/sử dụng Mic USB Soundcard USB hoặc 2/sử dụng phiên bản Pi có nhiều hơn 1 Sound card hoặc cả 1/ và 2/)

Chạy lệnh sau để biết ID của Mic USB
```sh
arecord -l
```
sau đó chạy lệnh sau để biết ID của Loa

```sh
aplay -l
```
Lưu lại thông tin về card_id và device_id ở mỗi kết quả lệnh

4.2.2. Khai báo cho Mic USB (Nếu ko sử dụng Mic USB thì bỏ qua phần này)

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

4.2.3. Copy file thiết lập cho mọi account (Nếu chỉ dùng Account Pi thì bỏ qua bước này)

Chạy lệnh sau
```sh
sudo cp /home/pi/.asoundrc /etc/asound.conf
```
4.2.4. Fix lỗi Audio không chạy tự động của Mic USB

Chạy lệnh sau

```sh
cd /home/pi/       
git clone https://github.com/shivasiddharth/PulseAudio-System-Wide       
cd ./PulseAudio-System-Wide/      
sudo cp ./pulseaudio.service /etc/systemd/system/pulseaudio.service    
sudo systemctl --system enable pulseaudio.service       
sudo systemctl --system start pulseaudio.service       
sudo cp ./client.conf /etc/pulse/client.conf        
sudo sed -i '/^pulse-access:/ s/$/root,pi/' /etc/group    
```
4.2.5. Reboot lại Pi
Chạy lệnh sau
```sh
sudo reboot
```

4.3. Cài đặt điều khiển Led cho Modun ReSpeaker Mic Array v2.0 hoặc ReSpeaker USB Mic Array (Nếu không dùng thì bỏ qua)

4.3.1. Đưa Account đang dùng (Ví dụ pi) vào group root

Chạy lệnh sau
```sh
sudo usermod -aG root account_name
```

4.4. Test loa và mic

4.4.1. Test loa
Chạy lệnh sau
```sh
speaker-test -t wav -c 2
```
4.4.2. Test Mic
Chạy lệnh sau để ghi âm
```sh
arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
```
Chạy lệnh sau để phát lại
```sh
aplay --format=S16_LE --rate=16000 out.raw
```
4.4.3. Test stream giữa Mic và Loa
```sh
arecord --format=S16_LE --rate=16000 | aplay --format=S16_LE --rate=16000
```
