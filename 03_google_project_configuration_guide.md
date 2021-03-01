### Đây là hướng dẫn đăng ký và Active Google Action

### STEP0. Bạn nào không muốn trải nghiệm việc cài đặt

Có thể sử dụng file .json trong Step 2 của người khác đã đăng ký thành công và bỏ qua Guide này chuyển sang các Guide tiếp theo

### STEP1. Đăng nhập và tạo GOOLGE ACTION PROJECT

1.1. Tạo Project Google Console

1.2. Truy cập vào địa chỉ: https://console.actions.google.com

1.3. Đăng nhập vào tài khoản Google của bạn. 

Có thể tạo mới hoặc dùng tài khoản hiện có, tuy nhiên tài khoản này nên là tài khoản đã đăng ký sử dụng Google Assistant trên loa Google Home hay điện thoại để đồng bộ được các tính năng của Google Assistant.

1.4. Chọn New Project – Dự án mới.

Nếu đã từng có một Project thuộc Google Develop COnsole rồi thì có thể sử dụng luôn mà không cần tạo mới bằng cách nhập lại tên để cửa sổ các dự án hiện ra và chọn

![TẠO PROJECT](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/01-Actions-on-Google.png)

Nếu tạo dự án mới, nhập tên cho Dự án này, ví dụ: Test Google Assistant, rồi ấn Create Project – Tạo dự án mới.

![TẠO PROJECT](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/create_new_project_01.jpg)

Google khống chế chỉ cho phép 5 dự án, do đó cố gắng tạo ít dự án cho nhiều mục đích

Nếu đây là dự án đầu tiên tạo trên Google Actions, bạn sẽ được yêu cầu đọc và Đồng ý với các điều khoản sử dụng dịch vụ – Terms of service. Chọn Quốc gia là Vietnam rồi ấn Agree and Continue – Đồng ý và tiếp tục.

Ở màn hình Development experience tiếp theo chọn Custom.

![TẠO PROJECT](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/select_project_type_01.jpg)

Sau đó chọn None

![TẠO PROJECT](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/select_project_type_02.jpg)

1.5. Chờ vài s, cửa sổ dự án sẽ mở ra ở mục Develop

Tiến hành nhập tên sẽ dùng để Google gọi cho App, có dạng Dr.

![TẠO PROJECT](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/create_name.jpg)

1.6. Chuyển sang Tab Deploy

![TAP DEPLOY](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_02.jpg)

Kéo xuống dưới cùng, ấn vào nút Save

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_02.jpg)

Web sẽ ra thông báo các mục bắt buộc cần phải nhập, có màu vàng. Tiến hành nhập các mục này bao gồm

Logo

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_021.jpg)

Developer Email, Developer Name, Privacy Policy

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_022.jpg)

Category

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_023.jpg)

Sau đó bấm lại Save

1.7. Chuyển sang Tab Test

Bấm Tab Talk to Dr.XXX

![TEST](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/test_app_01.jpg)

Cửa sổ Alright. Here's the test version of Dr.XXX hiện ra

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/test_app_02.jpg)

1.8. Quay lại mục Overrview

Khi này mọi thông tin đã bổ sung xong 

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/overview_01.jpg)

1.9. Ấn vào Create Release trong phần Beta

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_04.jpg)

Chọn Submit để quay lại Tab Deploy

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_05.jpg)

1.10. Ấn vào Create Release trong phần Production

Kích vào nút Submit for review để quay lại tab Deploy

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_06.jpg)

Quay lại Tab Deploy là hoàn tất việc khai báo trên Google Action Console

![CHECK ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/deploy_07.jpg)

![FINISH ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/finish_action.jpg)


### STEP2. Đăng nhập và tạo Google API

2.1. Truy cập vào link: https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview

Chọn Project vừa dùng trên STEP 1 (Lưu ý check theo project ID ở mục Username)

![CHỌN PROJECT ](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/google_project_01.jpg)

2.3. Chọn mục Library bên trái

![LIBRARY](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/active_api_01.jpg)

2.4. Tại khung tìm kiếm, gõ Google Asssistant API

![Google API](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/active_api_02.jpg)

2.5. Chọn Active

![Active](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/active_api_03.jpg)

### STEP3. Tạo và khai báo Credential

2.5. Chọn mục Credentials bên trái, sau đó chọn Create Identifiers


2.6. Chọn OAuth client ID

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_01.jpg)

2.7. Ấn vào nút configure the Authozation

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_02.jpg)

2.8. Chọn External

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_03.jpg)

2.9. Chọn User support email Addresss

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_04.jpg)

2.10. Chọn Developer contact details

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_05.jpg)

Hoàn tất đăng ký mục Access level

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_06.jpg)

2.11. Bấm Next để bỏ qua mục số 3 Optinal information

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_07.jpg)

2.12. Sang mục summary và kết thúc

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_08.jpg)

2.13. Ấn vào nút go back to the dashboard và kết thúc

![OAuth Client ID](https://github.com/phanmemkhoinghiep/google_assistant_vietnamese_speaking/blob/main/image/credential_09.jpg)

### STEP4. Khai báo quyền mà ứng dụng sẽ sử dụng

4.1. Khai báo Google Activity Control

4.2. Truy cập vào link: https://myaccount.google.com/activitycontrols với Acc sẽ sử dụng trong STEP 3, tốt nhất là trùng với Acc dùng để tạo Project ở trên

4.3. Kích hoạt các mục sau

4.4. Web & App Activity: Cần thiết lựa chọn thêm mục Include Chrome history and activity from sites, apps, and devices that use Google services, Enable Audio Recording

4.5. Device Information

4.6. Voice & Audio Activity

4.7. Youtube History

