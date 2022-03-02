

### Mặc định Source Code của Google Assistant đã có 02 Hotword là "OK Google" và "Hey Google", tuy nhiên có hỗ trợ khai thêm các hotword khác, sử dụng các Hotword của Porcupine cho Raspberry


### STEP1. Download hotword file

1.1. Download Hotword Snowboy

1.1.1. Truy cập trang Web https://github.com/Kitt-AI/snowboy/tree/master/resources/models

1.1.2. Ấn vào link file bất kỳ: Ví dụ snowboy.umdl 

1.1.3. Ấn vào mục Download ở bên phải, trình duyệt sẽ tự Download xuống

1.2. Download Hotword Picovoice

1.2.1. Truy cập trang Web https://github.com/Picovoice/porcupine/tree/master/resources/keyword_files/raspberry-pi 

1.2.2. Ấn vào link file bất kỳ: Ví dụ  alexa_raspberry-pi.ppn

1.2.3. Ấn vào mục Download ở bên phải, trình duyệt sẽ tự Download xuống

1.2.4. Truy nhập trang Web Picovoice https://console.picovoice.ai/

1.2.5. Đăng ký tài khoản

1.2.6. Lấy Access Token và lưu lại

### STEP2. Copy file

2.1. Copy file alexa_raspberry-pi.ppn từ PC sang Pi Zero Wireless bằng WinSCP

### STEP3. Khai báo cho hotword mới

3.1. Truy cập vào thư mục vietbot trên M Pi Zero Wireless

3.2. Mở file create_config.py bằng WinSCP và Notepad ++


```sh

data['hotword_engine'] = []
data['hotword_engine'].append({
    'name': 'snowboy',
    'is_active': True
})
data['hotword_engine'].append({
    'name': 'porcupine',
    'is_active': False,
    'porcupine_access_key': 'Giá trị của Access Key'    
data['hotword'] = []
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'snowboy.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'subex.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})

```

3.3. Save lại file create_config.py

### STEP4. Kết thúc

4.1. Lặp lại các Step 1,2,3 cho các Hotword khác

4.2. Sau khi khai báo xong hotword cuối cùng, save lại file create_config.py và chạy lại lệnh để tạo config

```sh
python3 create_config.py
```
