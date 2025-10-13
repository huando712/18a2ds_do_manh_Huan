Hướng dẫn nhanh — `chuong2/vidu.xml`

Files:
- `vidu.xml`: chứa các phần tử <company> với các thuộc tính `director` và `email`.
- `parse_vidu.py`: script Python đọc `vidu.xml`, in bảng ra console và ghi `vidu.csv`.

Sử dụng (PowerShell trên Windows):

```powershell
# Chạy script và ghi ra vidu.csv trong cùng thư mục
python .\chuong2\parse_vidu.py

# Hoặc chỉ định đường dẫn xuất
python .\chuong2\parse_vidu.py --out .\chuong2\output.csv
```

Lưu ý: đảm bảo Python có thể chạy bằng lệnh `python` trong PATH. Nếu cần, bạn có thể dùng đường dẫn tới python.exe cụ thể.
