### Đây là hướng dẫn đăng ký và Active Google Action

### STEP0. Bạn nào không muốn trải nghiệm việc cài đặt

Có thể sử dụng file .json trong Step 2 của người khác đã đăng ký thành công và bỏ qua Guide này

### STEP1. Đăng nhập và tạo GOOLGE ACTION PROJECT

1.1. Tạo Project Google Console

1.2. Truy cập vào địa chỉ: https://console.actions.google.com

1.3. Đăng nhập vào tài khoản Google của bạn. 

Có thể tạo mới hoặc dùng tài khoản hiện có, tuy nhiên tài khoản này nên là tài khoản đã đăng ký sử dụng Google Assistant trên loa Google Home hay điện thoại để đồng bộ được các tính năng của Google Assistant.

1.4. Chọn New Project – Dự án mới.

Nếu đã từng có một Project thuộc Google Develop COnsole rồi thì có thể sử dụng luôn mà không cần tạo mới bằng cách nhập lại tên để cửa sổ các dự án hiện ra và chọn

![TẠO PROJECT](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/01-Actions-on-Google.png)

Nếu tạo dự án mới, nhập tên cho Dự án này, ví dụ: Google Assistant, rồi ấn Create Project – Tạo dự án mới.

Google khống chế chỉ cho phép 5 dự án, do đó cố gắng tạo ít dự án cho nhiều mục đích

Nếu đây là dự án đầu tiên tạo trên Google Actions, bạn sẽ được yêu cầu đọc và Đồng ý với các điều khoản sử dụng dịch vụ – Terms of service. Chọn Quốc gia là Vietnam rồi ấn Agree and Continue – Đồng ý và tiếp tục.

Ở màn hình Development experience tiếp theo chọn SmartHome.

1.5. Lưu lại id của project: project_id để sử dụng về sau

1.6. Tiếp tục hoàn thiện 1 số thông tin cơ bản của Project cho đến khi Test và Public chờ xét duyệt được App ứng với Project vừa tạo

### STEP2. Đăng nhập và tạo GOOLGE ACTION PROJECT

2.1. Kích hoạt Google Assistant API cho Project tương ứng

2.3. Truy cập vào link: https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview

2.3. Chọn mục Library bên trái

2.4. Tại khung tìm kiếm, gõ Google Asssistant API, sau đó chọn Enable

![Google API](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/03-Activate-Google-Assistant-API.png)

2.5. Chọn mục Credentials bên trái

2.6. Khai báo các thông tin cần thiết

![KHAI BÁO OAUTH](https://developers.google.com/assistant/sdk/images/consent-oauth.png)

### STEP3. Khai báo quyền mà ứng dụng sẽ sử dụng

3.1. Khai báo Google Activity Control

3.2. Truy cập vào link: https://myaccount.google.com/activitycontrols với Acc sẽ sử dụng trong STEP 3, tốt nhất là trùng với Acc dùng để tạo Project ở trên

3.3. Kích hoạt các mục sau

3.4. Web & App Activity: Cần thiết lựa chọn thêm mục Include Chrome history and activity from sites, apps, and devices that use Google services, Enable Audio Recording

3.5. Device Information

3.6. Voice & Audio Activity

1.3.2.4. Youtube History

