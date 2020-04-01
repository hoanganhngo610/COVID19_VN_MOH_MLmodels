# (English/[Tiếng Việt](#vnese)) Training set/testing set processor

Version 1.1, released 1/4/2020.

### Requirements

* A `df_total.csv` file to be separated.

### How to run

* Open `getTrainTest.exe`
* Type in the folder directory where `df_total.csv` is stored. For example, if you store the file in C:/Workspace/Storage, type: `C:\Workspace\Storage\`.
* Then, type in the directory where you want to export your `df_train.csv` and `df_test.csv` files.

That's all. Enjoy!

*Tuan Khoi Nguyen, March 31st 2020.*

# <a name="vnese"></a> (Vietnamese) Hướng dẫn sử dụng phân tách dataset dành cho Chuyên gia phân tích COVID-19 tại Việt Nam

Phần mềm được tạo ra với mục đích phân tách file dữ liệu đã qua sàng lọc `df_total.csv` thành 2 file dữ liệu riêng biệt, phục vụ cho mục đích cải thiện và kiểm tra độ chính xác cho các mô hình dự đoán dịch bệnh SARS-CoV-2 tại Việt Nam.

### Hướng dẫn sử dụng
* Chạy file `getTrainTest.exe`.
* Nhập địa chỉ thư mục chứa file `df_total.csv`. Ví dụ: Nếu như tệp nằm trong thư mục C:/Workspace/Storage, gõ vào đây `C:\Workspace\Storage\`.
* Nhập địa chỉ thư mục muốn dùng để lưu trữ thành phẩm. Ở đây, 2 file `df_train.csv` và `df_test.csv` sẽ được tạo ra.

### Nguyên lý hoạt động
Trong một mô hình máy học, có thể chia ra dữ liệu ra thành 2 phần: 1 phần training set dùng để cải thiện độ chính xác trong tiên đoán của mô hình, và testing set để kiểm tra độ chính xác của mô hình.

Trong dự án này, training set và testing set sẽ được phân loại từ các bệnh nhân đã xuất viện và các bệnh nhân đang điều trị, phục vụ cho mục đích dự đoán dịch bệnh tại Việt Nam.

*Được tạo ra và biên soạn bởi Nguyễn Tuấn Khôi, ngày 31 tháng 3 năm 2020.*
