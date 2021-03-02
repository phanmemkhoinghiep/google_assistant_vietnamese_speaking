
### STEP1. Download code về Pi 

Download Code về Pi theo cách sau:
Trên console của Pi, sử dụng lệnh sau
```sh
git clone https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking.git
```

1.2.3. Khai báo file wpa_supplicant.conf như hướng dẫn tại Step 1.3.2 ở Link:

https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/02_software_enviroment_installation_guide.md

1.2.4. Cắm thẻ nhớ vào Pi Zero W và boot lên

### STEP2.  Kiểm tra ứng dụng đã chạy được mà không báo lỗi về thư viện

2.1. Truy cập vào thư mục source sử dụng lệnh sau

```sh
cd /home/pi/google_assistant_vietnamese_speaking/src
```

2.2. Chạy trực tiếp

```sh
python3 python3 pushtotalk.py 
'''
Nếu ra kết quả sau

```sh
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
ERROR:root:Error loading credentials: [Errno 2] No such file or directory: '/home/pi/.config/google-oauthlib-tool/credentials.json'
ERROR:root:Run google-oauthlib-tool to initialize new OAuth 2.0 credentials.
```
Là hệ thống đã hoạt động tốt với các thư viện. Chúng ta cần đăng ký thiết bị theo 1 trong 2 cách sau:

### STEP3.  Cách 1: Đăng ký thiết bị sử dụng Web Google

3.1. Mở trang https://console.actions.google.com/u/0/project/project_id/deviceregistration/ với project_id là project_id vừa lưu ở 2.1.1.

và điền lần lượt từng mục

![ĐĂNG KÝ THIẾT BỊ](https://developers.google.com/assistant/sdk/images/console/device-models-aog.png)

![ĐĂNG KÝ THIẾT BỊ](https://user-images.githubusercontent.com/64348125/109378336-3f136d80-7904-11eb-808e-37bf5c726bf3.png)

3.1.1. Product Name: Gõ tùy ý

3.1.2. Manufacturer name: Gõ  tùy ý

3.1.3. Device Type: Chọn Speaker

3.1.4. Device Model ID: Để mặc định hoặc tùy chọn. Nhớ lưu lại thông tin để dùng sau

3.1.5. Bấm Register Model

3.2. Download file về máy

3.3. Cửa sổ mới mở ra, chọn Download OAuth 2.0 credentials

![ĐĂNG KÝ THIẾT BỊ](https://user-images.githubusercontent.com/64348125/109378347-56525b00-7904-11eb-9764-c2af673d9ac4.png)


3.4. File .json được lưu về máy, giữ nguyên File không đổi tên 

3.5. Copy file json vừa download được sang thư mục của loa thông minh tại đường dẫn /home/pi

3.6. Có thể lấy lại file json bằng cách vào lại bước 2.1, chọn Download OAuth 2.0 credentials

![LẤY LẠI FILE](https://developers.google.com/assistant/sdk/images/console/edit-model.png)


### STEP4.  Cách 2: Đăng ký thiết bị sử dụng Tool

https://developers.google.com/assistant/sdk/reference/device-registration/device-tool


### STEP5. Kích hoạt Google Assistant trên loa thông minh

5.1. Truy nhập SSH của Raspberry Pi

5.1.1 Gõ lệnh sau

```sh
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets /home/pi/client_secret_client-id.json

```
với client_secret_client-id.json là tên file json vừa lưu ở /home/pi theo bước 2.2.3.

5.1.2. Kết quả dòng lệnh sẽ trả về có dạng

```sh
Please visit this URL to authorize this application: https://...
```
5.2. Lấy mã từ Google

5.2.1. Copy toàn bộ đường link bắt đầu từ https:// sau đó dán vào trình duyệt trên máy PC, 

5.2.2. Cửa sổ đăng nhập hiện ra, đăng nhập vào tài khoản Google (Là tài khoản duy nhất từ Step 1) sau đó bấm Allow(Cho phép) và Tiếp tục(Continue) để cho phép quyền truy cập vào tài khoản từ App Google Action

5.2.3. Sau khi chấp thuận, một mã sẽ hiện ra có dạng

```sh
4/XXXX
```
5.2.4. Copy mã trên vào cửa sổ dòng lệnh còn đang chạy trên Raspberry Pi tại mục:

```sh
Enter the authorization code:

```
5.2.5. Nếu toàn bộ các bước trên đúng, hệ thống sẽ gen ra một file có tên là credentials.json, nằm trong thư mục ẩn .config tại đường dẫn /home/pi/.config/google-oauthlib-tool/

theo thông báo trên console

```sh
credentials saved: /path/to/.config/google-oauthlib-tool/credentials.json

```
Chú ý, không được xóa, đổi tên file này trong quá trình sử dụng Google Assistant

5.3. Trong trường hợp muốn dùng Account Google khác

5.3.1. Thay Acc khác

Xóa thư mục trên bằng lệnh

```sh
sudo rm -rf/home/pi/.config/google-oauthlib-tool/credentials.json

```
Chạy lại toàn bộ các bước từ 3.1. đến 3.2 để tạo được file credentials.json mới

5.3.2. Dùng nhiều Acc

Đổi tên file .json hiện tại bằng lệnh

```sh
sudo cp /home/pi/.config/google-oauthlib-tool/credentials.json /home/pi/.config/google-oauthlib-tool/credentials_1.json

```
Chạy lại toàn bộ các bước từ 5.1. đến 5.2 để tạo được file credentials.json mới

Lặp lại bước 5.3.2 để tạo ra file credentials_x.json

Muốn dùng Acc nào thì tạo file credentials.json từ file đó

```sh
sudo cp /home/pi/.config/google-oauthlib-tool/credentials_x.json /home/pi/.config/google-oauthlib-tool/credentials.json

```

5.2.6. Trong trường hợp báo lỗi InvalidGrantError, là do mã copy vào theo bước 3.1.5. bị sai, cần phải lặp lại từ 3.1. Chú ý mã copy không có khoảng trắng, khi select bằng chuột có thể có khoảng trắng

### STEP6. Kết thúc

6.1. Có thể chạy ứng dụng theo link tại:

https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/05_running_guide.md
