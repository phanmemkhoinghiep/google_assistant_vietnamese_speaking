

### Mặc định Source Code của Google Assistant đã có 02 Hotword là "OK Google" và "Hey Google", tuy nhiên có hỗ trợ khai thêm các hotword khác, sử dụng các Hotword của Porcupine cho Raspberry

### STEP1. Download hotword file

1.1 Truy cập trang Web https://github.com/Picovoice/porcupine/tree/master/resources/keyword_files/raspberry-pi

1.2. Ấn vào link file bất kỳ: Ví dụ alexa_raspberry-pi.ppn https://github.com/Picovoice/porcupine/blob/master/resources/keyword_files/raspberry-pi/alexa_raspberry-pi.ppn

1.3. Ấn vào mục Download ở bên phải, trình duyệt sẽ tự Download xuống

### STEP2. Copy file

2.1. Copy file alexa_raspberry-pi.ppn từ PC sang Pi Zero Wireless bằng WinSCP

### STEP3. Khai báo cho một hotword mới (Alexa với tên file là alexa_raspberry-pi.ppn)

3.1. Truy cập vào thư mục /home/pi/google_assistant_vietnamese_speaking/src trên Raspberry

3.2. Mở file config.yaml bằng WinSCP và Notepad ++ và chèn thêm một dòng sau dòng sensitivities và sau dòng keyword_paths :

```sh
sensitivities:
 - 0.3
```
và 
```sh
keyword_paths:
 - alexa_raspberry-pi.ppn
```

3.3. Save lại file config.yaml

### STEP4. Kết thúc

4.1. Lặp lại các Step 1.2.3 cho các Hotword khác

Lưu ý: Số dòng dưới mục sensitivities:  và số dòng dưới mục keyword_paths: phải bằng nhau

4.2. Sau khi khai báo xong hotword cuối cùng, save lại file config.yaml và chạy lại Google Asistant theo đường link

https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/05_running_guide.md
