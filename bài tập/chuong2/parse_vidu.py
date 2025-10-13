# -*- coding: utf-8 -*-
"""
Script nhỏ để phân tích `vidu.xml` và xuất ra bảng/CSV.
Sử dụng: python parse_vidu.py [--out output.csv]

In Vietnamese: đọc file XML trong cùng thư mục và in ra:
- Tên công ty (nội dung node)
- director (thuộc tính)
- email (thuộc tính)

Kết quả cũng sẽ được ghi ra CSV nếu bạn cung cấp --out hoặc mặc định là vidu.csv
"""
import argparse
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

THIS_DIR = Path(__file__).parent
XML_PATH = THIS_DIR / "vidu.xml"


def parse_xml(path: Path):
    tree = ET.parse(path)
    root = tree.getroot()
    rows = []
    for company in root.findall('company'):
        name = (company.text or '').strip()
        director = company.get('director', '').strip()
        email = company.get('email', '').strip()
        rows.append({'company': name, 'director': director, 'email': email})
    return rows


def print_table(rows):
    # Compute widths
    w_name = max(len(r['company']) for r in rows) if rows else 6
    w_dir = max(len(r['director']) for r in rows) if rows else 8
    w_email = max(len(r['email']) for r in rows) if rows else 5

    header = f"{'Company'.ljust(w_name)}  {'Director'.ljust(w_dir)}  {'Email'.ljust(w_email)}"
    sep = '-' * len(header)
    print(header)
    print(sep)
    for r in rows:
        print(f"{r['company'].ljust(w_name)}  {r['director'].ljust(w_dir)}  {r['email'].ljust(w_email)}")


def write_csv(rows, out_path: Path):
    with out_path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['company', 'director', 'email'])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Phân tích chuong2/vidu.xml và xuất CSV')
    parser.add_argument('--out', '-o', help='Đường dẫn file CSV xuất ra (mặc định: vidu.csv)', default='vidu.csv')
    args = parser.parse_args()

    if not XML_PATH.exists():
        print(f"Không tìm thấy file XML: {XML_PATH}")
        raise SystemExit(1)

    rows = parse_xml(XML_PATH)
    print_table(rows)

    out = Path(args.out)
    if not out.is_absolute():
        out = THIS_DIR / out
    write_csv(rows, out)
    print()
    print(f"Đã ghi {len(rows)} dòng vào: {out}")
