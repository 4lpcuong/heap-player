
# Heap Builder

## Mô Tả
Chương trình này được thiết kế để xây dựng max heap và min heap từ một dãy số nhập vào, phục vụ cho việc kiểm tra kết quả làm bài với Max/Min heap. Ngoài ra, chương trình cũng hỗ trợ tính năng extract, cho phép lấy ra và loại bỏ phần tử đầu tiên từ heap. Chương trình sử dụng `colorama` để tạo màu sắc trong đầu ra và `tabulate` để hiển thị heap dưới dạng bảng.

## Cài Đặt
Chương trình yêu cầu Python 3. Để cài đặt các thư viện cần thiết, hãy chạy lệnh sau:

```bash
pip install colorama tabulate
git clone https://github.com/4lpcuong/heap-player.git
```

## Sử Dụng
Chương trình có thể được chạy từ dòng lệnh và có hai chế độ hoạt động:

- **Max Heap**: Xây dựng max heap từ dãy số.
- **Min Heap**: Xây dựng min heap từ dãy số.
- **Extract**: Lấy ra và loại bỏ phần tử đầu tiên từ heap sau khi xây dựng nó.

### Cú Pháp
```bash
python heapplayer.py -M [numbers...] [-e]
python heapplayer.py --max [numbers...] [--extract]

python heapplayer.py -m [numbers...] [-e]
python heapplayer.py --min [numbers...] [--extract]
```

Trong đó, tùy chọn `-e` hoặc `--extract` sẽ kích hoạt tính năng extract.

### Ví Dụ
```bash
python heapplayer.py --max 33 96 14 29 78 94 34 42 93 99 --extract
python heapplayer.py --min 33 96 14 29 78 94 34 42 93 99 --extract
```

## Tác Giả
Cuong Lam Phu

## Giấy Phép
Dự án này được cấp phép theo điều khoản của giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.
