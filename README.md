
# Heap Builder

## Mô Tả
Chương trình này được thiết kế để xây dựng max heap và min heap từ một dãy số nhập vào dể phục vụ cho việc kiểm tra kết quả làm bài với Max/Min heap. Chương trình sử dụng `colorama` để tạo màu sắc trong đầu ra và `tabulate` để hiển thị heap dưới dạng bảng.

## Cài Đặt
Chương trình yêu cầu Python 3. Để cài đặt các thư viện cần thiết, hãy chạy lệnh sau:

```bash
pip install colorama tabulate
git clone https://github.com/itsphucuong/heap-player.git
```

## Sử Dụng
Chương trình có thể được chạy từ dòng lệnh và có hai chế độ hoạt động:

1. **Max Heap**: Xây dựng max heap từ dãy số.
2. **Min Heap**: Xây dựng min heap từ dãy số.

### Cú Pháp
```bash
python heapplayer.py -M [numbers...]
python heapplayer.py --max [numbers...]

python heapplayer.py -m [numbers...]
python heapplayer.py --min [numbers...]
```
![image](https://github.com/itsphucuong/heap-player/assets/118279100/97595674-55d4-40ea-ae40-05cba827174f)

### Ví Dụ
```bash
python heapplayer.py --max 33 96 14 29 78 94 34 42 93 99
python heapplayer.py --min 33 96 14 29 78 94 34 42 93 99
```
![image](https://github.com/itsphucuong/heap-player/assets/118279100/5782522d-fe04-4901-925a-9c876032d648)

![image](https://github.com/itsphucuong/heap-player/assets/118279100/4e99fd7a-a942-49a6-b50e-4741bd4c3599)


## Tác Giả
Cuong Lam Phu

## Giấy Phép
Dự án này được cấp phép theo điều khoản của giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.
