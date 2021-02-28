### Đây là hướng dẫn đăng ký và Active Google Action

### STEP0. Bạn nào không muốn trải nghiệm việc cài đặt

Có thể sử dụng file .json trong Step 2 của người khác đã đăng ký thành công và bỏ qua Guide này

### STEP1. Đăng nhập và tạo GOOLGE ACTION PROJECT

1.1. Tạo Project Google Console

1.1.1. Truy cập vào địa chỉ: https://console.actions.google.com

1.1.2. Đăng nhập vào tài khoản Google của bạn. 

Có thể tạo mới hoặc dùng tài khoản hiện có, tuy nhiên tài khoản này nên là tài khoản đã đăng ký sử dụng Google Assistant trên loa Google Home hay điện thoại để đồng bộ được các tính năng của Google Assistant.

1.1.3. Chọn New Project – Dự án mới.

Nếu đã từng có một Project thuộc Google Develop COnsole rồi thì có thể sử dụng luôn mà không cần tạo mới bằng cách nhập lại tên để cửa sổ các dự án hiện ra và chọn

![TẠO PROJECT](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/01-Actions-on-Google.png)

Nếu tạo dự án mới, nhập tên cho Dự án này, ví dụ: Google Assistant, rồi ấn Create Project – Tạo dự án mới.

Google khống chế chỉ cho phép 5 dự án, do đó cố gắng tạo ít dự án cho nhiều mục đích

Nếu đây là dự án đầu tiên tạo trên Google Actions, bạn sẽ được yêu cầu đọc và Đồng ý với các điều khoản sử dụng dịch vụ – Terms of service. Chọn Quốc gia là Vietnam rồi ấn Agree and Continue – Đồng ý và tiếp tục.

Ở màn hình Development experience tiếp theo chọn SmartHome.

1.1.4. Tiếp tục hoàn thiện 1 số thông tin cơ bản của Project cho đến khi Test và Public chờ xét duyệt được App ứng với Project vừa tạo

1.2. Kích hoạt Google Assistant API cho Project tương ứng

1.2.1. Truy cập vào link: https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview

1.2.2. Chọn mục Library bên trái

1.2.3. Tại khung tìm kiếm, gõ Google Asssistant API, sau đó chọn Enable

![TẠO PROJECT](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/03-Activate-Google-Assistant-API.png)

1.2.4. Chọn mục Credentials bên trái

1.2.5. Khai báo các thông tin cần thiết

![KHAI BÁO OAUTH](https://developers.google.com/assistant/sdk/images/consent-oauth.png)

1.3. Khai báo Google Activity Control

1.3.1. Truy cập vào link: https://myaccount.google.com/activitycontrols với Acc sẽ sử dụng trong STEP 3, tốt nhất là trùng với Acc dùng để tạo Project ở trên

1.3.2. Kích hoạt các mục sau

1.3.2.1. Web & App Activity: Cần thiết lựa chọn thêm mục Include Chrome history and activity from sites, apps, and devices that use Google services, Enable Audio Recording

1.3.2.2. Device Information

1.3.2.3. Voice & Audio Activity

1.3.2.4. Youtube History

### STEP2. Đăng ký thiết bị

2.1. Đăng ký thiết bị trên Web Google

2.1.1. Lưu lại id của project: project_id

2.1.2. Mở trang https://console.actions.google.com/u/0/project/project_id/deviceregistration/ với project_id là project_id vừa lưu ở 2.1.1.

và điền lần lượt từng mục

![ĐĂNG KÝ THIẾT BỊ](https://developers.google.com/assistant/sdk/images/console/device-models-aog.png)

![ĐĂNG KÝ THIẾT BỊ](https://user-images.githubusercontent.com/64348125/109378336-3f136d80-7904-11eb-808e-37bf5c726bf3.png)

2.1.3. Product Name: Gõ tùy ý

2.1.4. Manufacturer name: Gõ  tùy ý

2.1.5. Device Type: Chọn Speaker

2.1.6. Device Model ID: Để mặc định hoặc tùy chọn. Nhớ lưu lại thông tin để dùng sau

2.1.7. Bấm Register Model

2.2. Download file về máy

2.2.1. Cửa sổ mới mở ra, chọn Download OAuth 2.0 credentials

![ĐĂNG KÝ THIẾT BỊ](https://user-images.githubusercontent.com/64348125/109378347-56525b00-7904-11eb-9764-c2af673d9ac4.png)


2.2.2. File .json được lưu về máy, giữ nguyên File không đổi tên 

2.2.3. Copy file json vừa download được sang thư mục của loa thông minh tại đường dẫn /home/pi

2.2.4. Có thể lấy lại file json bằng cách vào lại bước 2.1, chọn Download OAuth 2.0 credentials

![LẤY LẠI FILE](https://developers.google.com/assistant/sdk/images/console/edit-model.png)

### STEP3. Kích hoạt Google Assistant trên loa thông minh

3.1. Truy nhập SSH của Raspberry Pi

3.1.1 Gõ lệnh sau

```sh
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets /home/pi/client_secret_client-id.json

```
với client_secret_client-id.json là tên file json vừa lưu ở /home/pi theo bước 2.2.3.

3.1.2. Kết quả dòng lệnh sẽ trả về có dạng

```sh
Please visit this URL to authorize this application: https://...
```
3.2. Lấy mã từ Google

3.2.1. Copy toàn bộ đường link bắt đầu từ https:// sau đó dán vào trình duyệt trên máy PC, 

3.2.2. Cửa sổ đăng nhập hiện ra, đăng nhập vào tài khoản Google (Là tài khoản duy nhất từ Step 1) sau đó bấm Allow(Cho phép) và Tiếp tục(Continue) để cho phép quyền truy cập vào tài khoản từ App Google Action

3.2.3. Sau khi chấp thuận, một mã sẽ hiện ra có dạng

```sh
4/XXXX
```
3.2.4. Copy mã trên vào cửa sổ dòng lệnh còn đang chạy trên Raspberry Pi tại mục:

```sh
Enter the authorization code:

```
3.2.5. Nếu toàn bộ các bước trên đúng, hệ thống sẽ gen ra một file có tên là credentials.json, nằm trong thư mục ẩn .config tại đường dẫn /home/pi/.config/google-oauthlib-tool/

theo thông báo trên console

```sh
credentials saved: /path/to/.config/google-oauthlib-tool/credentials.json

```
Chú ý, không được xóa, đổi tên file này trong quá trình sử dụng Google Assistant

3.3. Trong trường hợp muốn dùng Account Google khác

3.3.1. Thay Acc khác

Xóa thư mục trên bằng lệnh

```sh
sudo rm -rf/home/pi/.config/google-oauthlib-tool/credentials.json

```
Chạy lại toàn bộ các bước từ 3.1. đến 3.2 để tạo được file credentials.json mới

3.3.2. Dùng nhiều Acc

Đổi tên file .json hiện tại bằng lệnh

```sh
sudo cp /home/pi/.config/google-oauthlib-tool/credentials.json /home/pi/.config/google-oauthlib-tool/credentials_1.json

```
Chạy lại toàn bộ các bước từ 3.1. đến 3.2 để tạo được file credentials.json mới

Lặp lại bước 3.3.2 để tạo ra file credentials_x.json

Muốn dùng Acc nào thì tạo file credentials.json từ file đó

```sh
sudo cp /home/pi/.config/google-oauthlib-tool/credentials_x.json /home/pi/.config/google-oauthlib-tool/credentials.json

```


3.2.6. Trong trường hợp báo lỗi InvalidGrantError, là do mã copy vào theo bước 3.1.5. bị sai, cần phải lặp lại từ 3.1. Chú ý mã copy không có khoảng trắng, khi select bằng chuột có thể có khoảng trắng

3.3. Kết thúc

3.3.1 Quá trình Active Google Assistant kết thúc, có thể chạy Google Assistant theo hướng dẫn:

https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/05_running_guide.md


