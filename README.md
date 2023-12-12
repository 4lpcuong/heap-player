
# Heap Builder

## Mô Tả
Chương trình này được thiết kế để xây dựng max heap và min heap từ một dãy số nhập vào. Nó sử dụng `colorama` để tạo màu sắc trong đầu ra và `tabulate` để hiển thị heap dưới dạng bảng đẹp mắt.

## Cài Đặt
Chương trình yêu cầu Python 3. Để cài đặt các thư viện cần thiết, hãy chạy lệnh sau:

```bash
pip install colorama tabulate
```

## Sử Dụng
Chương trình có thể được chạy từ dòng lệnh và có hai chế độ hoạt động:

1. **Max Heap**: Xây dựng max heap từ dãy số.
2. **Min Heap**: Xây dựng min heap từ dãy số.

### Cú Pháp
```bash
python chuongtrinh.py -M [numbers...]
python chuongtrinh.py --max [numbers...]

python chuongtrinh.py -m [numbers...]
python chuongtrinh.py --min [numbers...]
```

### Ví Dụ
```bash
python chuongtrinh.py --max 33 96 14 29 78 94 34 42 93 99
python chuongtrinh.py --min 33 96 14 29 78 94 34 42 93 99
```

## Tác Giả
Cuong Lam Phu

## Giấy Phép
Dự án này được cấp phép theo điều khoản của giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.
