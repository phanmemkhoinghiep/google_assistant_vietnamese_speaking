### ĐÂY LÀ HƯỚNG DẪN TỐI ƯU CHO PI

### STEP1. Cấu hình tối ưu cho Pi

1.1. Chạy config
Chạy lệnh sau
```sh
sudo raspi-config
```
1.2. Cài đặt thời gian với múi giờ VN

Chọn mục số 5 Localisation Options, Select rồi Enter

Chọn L2 Time Zone

Chọn Asia

Chọn Ho Chi Minh City, OK rồi Enter

1.3. Cài đặt Pi khởi động với Command line để tiết kiệm bộ nhớ

Chọn mục System Options, Select rồi Enter

Chọn S5 Boot/ Auto Login, Select rồi Enter

Chọn B2, OK

1.4. Giảm bộ nhớ RAM dùng cho đồ họa

Chọn mục Performance Options, Select rồi Enter

Chọn P2 GPU Memory, Select rồi Enter

Chọn 16, OK

1.5. Khởi động lại Pi

Khi thoát khỏi Raspi Config, chọn Yes để khởi động lại

1.6. Tăng bộ nhớ của Raspbian lên 1G

Gõ lệnh:
```sh
free -hm
```
Hệ thống sẽ trả về bộ nhớ Swap có dung lượng xấp xỉ 1G

```sh
               total        used        free      shared  buff/cache   available
Mem:           459Mi        57Mi       278Mi       1.0Mi       123Mi       351Mi
Swap:          100M          0B       100M
```
Tăng lên 1GB bằng cách gõ lệnh:

```sh
sudo dphys-swapfile swapoff
```
Tiếp đó gõ lệnh:
```sh
sudo nano /etc/dphys-swapfile
```
Tìm đến dòng sau và sửa lại 100 thành 1024
```sh
CONF_SWAPSIZE=1024
```
Lần lượt bấm đồng thời Ctrl + X sau đó bấm Y rồi bấm Enter

Sau đó gõ
```sh
sudo dphys-swapfile setup
```
Hệ thống sẽ báo lại
```sh
want /var/swap=1024MByte, checking existing: deleting wrong size file (104857600), generating swapfile ... of 1024MBytes
```
Chờ 1 lát cho đến khi quay về dấu nhắc lệnh thì gõ
```sh
sudo dphys-swapfile swapon
```
Sau đó reboot lại hệ thống
```sh
sudo reboot
```
Sau khi reboot thành công, dùng lại lệnh

```sh
free -hm
```
Hệ thống sẽ trả về bộ nhớ Swap có dung lượng xấp xỉ 1G

```sh
               total        used        free      shared  buff/cache   available
Mem:           459Mi        57Mi       278Mi       1.0Mi       123Mi       351Mi
Swap:          1.0Gi          0B       1.0Gi
```
