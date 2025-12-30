
# Bài 2.1 - 2.5: Ví dụ và giải pháp bằng Python
# Tập hợp mã này thực hiện các yêu cầu:
# Bài 2.1: Tạo file XML lưu thông tin công ty (giám đốc, địa chỉ, điện thoại, mã số thuế)
# Bài 2.2: Tạo file XML lưu danh sách sinh viên (mã, tên, năm sinh, lớp, giới tính)
# Bài 2.3: Tạo một file sample.xml mẫu (theo đề bài)
# Bài 2.4: Sử dụng xml.dom.minidom để phân tích và in cây phần tử của sample.xml
# Bài 2.5: Sử dụng getElementsByTagName() để lấy danh sách phần tử và in tên của từng phần tử

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from typing import Optional

# --- Helper functions ---

def pretty_print_minidom(dom_node: minidom.Document) -> str:
    """Trả về chuỗi XML đẹp (indent) từ một minidom document."""
    return dom_node.toprettyxml(indent="  ")


def ensure_dir_for_file(filepath: str) -> None:
    """Tạo thư mục chứa file nếu chưa tồn tại."""
    folder = os.path.dirname(os.path.abspath(filepath))
    if folder and not os.path.exists(folder):
        os.makedirs(folder)


# ----------------- Bài 2.1 -----------------

def create_company_xml(path: str, director: dict) -> None:
    """
    Tạo file XML lưu thông tin công ty.
    director: dict có keys: name, address, phone, tax_id
    """
    if not isinstance(director, dict):
        raise ValueError("director phải là dict chứa name, address, phone, tax_id")
    for key in ("name", "address", "phone", "tax_id"):
        if key not in director:
            raise ValueError(f"Thiếu trường '{key}' trong thông tin giám đốc")

    root = ET.Element('Company')
    info = ET.SubElement(root, 'Director')
    ET.SubElement(info, 'Name').text = str(director['name'])
    ET.SubElement(info, 'Address').text = str(director['address'])
    ET.SubElement(info, 'Phone').text = str(director['phone'])
    ET.SubElement(info, 'TaxID').text = str(director['tax_id'])

    tree = ET.ElementTree(root)
    ensure_dir_for_file(path)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f"Đã tạo file company XML: {path}")


# ----------------- Bài 2.2 -----------------

def create_students_xml(path: str, students: list) -> None:
    """
    Tạo file XML lưu danh sách sinh viên.
    students: list các dict, mỗi dict: {id, name, year, class, gender}
    """
    if not isinstance(students, list):
        raise ValueError("students phải là list các dict")

    root = ET.Element('Students')
    for s in students:
        if not isinstance(s, dict):
            continue
        sid = s.get('id')
        if sid is None:
            raise ValueError('Mỗi sinh viên phải có khóa id')
        stu = ET.SubElement(root, 'Student', attrib={'id': str(sid)})
        ET.SubElement(stu, 'Name').text = str(s.get('name', ''))
        ET.SubElement(stu, 'BirthYear').text = str(s.get('year', ''))
        ET.SubElement(stu, 'Class').text = str(s.get('class', ''))
        ET.SubElement(stu, 'Gender').text = str(s.get('gender', ''))

    tree = ET.ElementTree(root)
    ensure_dir_for_file(path)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f"Đã tạo file students XML: {path}")


# ----------------- Bài 2.3 -----------------

def create_sample_xml(path: str) -> None:
    """
    Tạo file sample.xml theo nội dung đề bài ví dụ (công ty + staff).
    """
    sample = '''<?xml version="1.0"?>
<company>
  <name>GeeksForGeeks Company</name>
  <staff id="1">
    <name>Amar Pandey</name>
    <salary>8.5 LPA</salary>
  </staff>
  <staff id="2">
    <name>Akbhar Khan</name>
    <salary>6.5 LPA</salary>
  </staff>
  <staff id="3">
    <name>Anthony Walter</name>
    <salary>3.2 LPA</salary>
  </staff>
</company>
'''
    ensure_dir_for_file(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sample)
    print(f"Đã tạo file mẫu sample.xml: {path}")


# ----------------- Bài 2.4 -----------------

def parse_with_minidom_and_print(path: str) -> None:
    """
    Dùng xml.dom.minidom để phân tích sample.xml và in cấu trúc (đẹp).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File không tồn tại: {path}")

    dom = minidom.parse(path)
    pretty = pretty_print_minidom(dom)
    print("--- Nội dung XML (đã format bằng minidom) ---")
    print(pretty)

    # In ra danh sách các phần tử con của root
    root = dom.documentElement
    print(f"Root element: {root.tagName}")
    print('Các phần tử con của root:')
    for node in root.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            print(f" - {node.tagName}")


# ----------------- Bài 2.5 -----------------

def list_elements_by_tagname(path: str, tag: str) -> None:
    """
    Sử dụng getElementsByTagName để lấy danh sách các phần tử và in tên + text.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File không tồn tại: {path}")

    dom = minidom.parse(path)
    elements = dom.getElementsByTagName(tag)
    print(f"Tìm {len(elements)} phần tử với tag '{tag}':")
    for i, el in enumerate(elements, 1):
        # Lấy text nội dung bên trong element (nối các child text nodes)
        text_parts = []
        for ch in el.childNodes:
            if ch.nodeType == ch.TEXT_NODE:
                text_parts.append(ch.data.strip())
        text = ' '.join([p for p in text_parts if p])
        # Nếu element có attribute, hiển thị
        attrs = []
        if el.attributes:
            for k in el.attributes.keys():
                attrs.append(f"{k}={el.getAttribute(k)}")
        attr_str = (" (" + ", ".join(attrs) + ")") if attrs else ""
        print(f"{i}. <{tag}>{attr_str} -> '{text}'")


# ----------------- Demo: Chạy các bước lần lượt -----------------

def demo(output_dir: Optional[str] = '.') -> None:
    output_dir = os.path.abspath(output_dir)
    print(f"Thư mục đầu ra: {output_dir}")

    # Bài 2.1
    company_path = os.path.join(output_dir, 'company_info.xml')
    director = {
        'name': 'Nguyen Van A',
        'address': '123 Đường ABC, Thành phố XYZ',
        'phone': '+84-912-345-678',
        'tax_id': '0102030405'
    }
    create_company_xml(company_path, director)

    # Bài 2.2
    students_path = os.path.join(output_dir, 'students.xml')
    students = [
        {'id': 'SV001', 'name': 'Tran Thi B', 'year': 2001, 'class': 'K61CNTT', 'gender': 'Nu'},
        {'id': 'SV002', 'name': 'Le Van C', 'year': 2000, 'class': 'K61CNTT', 'gender': 'Nam'},
        {'id': 'SV003', 'name': 'Pham Van D', 'year': 2002, 'class': 'K61HTTT', 'gender': 'Nam'},
    ]
    create_students_xml(students_path, students)

    # Bài 2.3
    sample_path = os.path.join(output_dir, 'sample.xml')
    create_sample_xml(sample_path)

    # Bài 2.4
    parse_with_minidom_and_print(sample_path)

    # Bài 2.5 - ví dụ lấy tag 'staff' và 'name'
    list_elements_by_tagname(sample_path, 'staff')
    list_elements_by_tagname(sample_path, 'name')


if __name__ == '__main__':
    # Khi chạy trực tiếp, tạo các file trong thư mục hiện hành
    demo('.')
