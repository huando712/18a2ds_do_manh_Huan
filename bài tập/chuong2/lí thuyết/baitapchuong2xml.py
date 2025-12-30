import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

# ===== Hàm hỗ trợ =====
def ensure_dir_for_file(filepath):
    """Tạo thư mục chứa file nếu chưa có."""
    folder = os.path.dirname(os.path.abspath(filepath))
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

# ==========================================
# 🧠 BÀI 2.1: Tạo file XML lưu thông tin công ty
# ==========================================
def create_company_xml(path, director):
    """
    Tạo file XML lưu thông tin công ty.
    director: dict gồm name, address, phone, tax_id
    """
    root = ET.Element('Company')
    info = ET.SubElement(root, 'Director')

    ET.SubElement(info, 'Name').text = director['name']
    ET.SubElement(info, 'Address').text = director['address']
    ET.SubElement(info, 'Phone').text = director['phone']
    ET.SubElement(info, 'TaxID').text = director['tax_id']

    tree = ET.ElementTree(root)
    ensure_dir_for_file(path)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f"✅ Đã tạo file XML công ty: {path}")


# ==========================================
# 🧠 BÀI 2.2: Tạo file XML lưu danh sách sinh viên
# ==========================================
def create_students_xml(path, students):
    """
    Tạo file XML lưu danh sách sinh viên.
    students: list các dict gồm id, name, year, class, gender
    """
    root = ET.Element('Students')

    for s in students:
        student = ET.SubElement(root, 'Student', attrib={'id': s['id']})
        ET.SubElement(student, 'Name').text = s['name']
        ET.SubElement(student, 'BirthYear').text = str(s['year'])
        ET.SubElement(student, 'Class').text = s['class']
        ET.SubElement(student, 'Gender').text = s['gender']

    tree = ET.ElementTree(root)
    ensure_dir_for_file(path)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f"✅ Đã tạo file XML sinh viên: {path}")


# ==========================================
# 🧠 BÀI 2.3: Tạo file sample.xml theo ví dụ đề bài
# ==========================================
def create_sample_xml(path):
    sample_content = """<?xml version="1.0"?>
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
</company>"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    print(f"✅ Đã tạo file mẫu sample.xml: {path}")


# ==========================================
# 🧠 BÀI 2.4: Dùng minidom để phân tích XML
# ==========================================
def parse_with_minidom(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Không tìm thấy file XML.")

    dom = minidom.parse(path)
    print("--- NỘI DUNG XML (đã format) ---")
    print(dom.toprettyxml(indent="  "))

    root = dom.documentElement
    print(f"Tên phần tử gốc: {root.tagName}")
    print("Các phần tử con:")
    for node in root.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            print(f" - {node.tagName}")


# ==========================================
# 🧠 BÀI 2.5: Lấy danh sách phần tử bằng getElementsByTagName()
# ==========================================
def list_elements_by_tagname(path, tag):
    if not os.path.exists(path):
        raise FileNotFoundError("Không tìm thấy file XML.")

    dom = minidom.parse(path)
    elements = dom.getElementsByTagName(tag)

    print(f"🔎 Tìm thấy {len(elements)} phần tử <{tag}>:")
    for i, el in enumerate(elements, 1):
        text = "".join(node.data.strip() for node in el.childNodes if node.nodeType == node.TEXT_NODE)
        attrs = {k: el.getAttribute(k) for k in el.attributes.keys()} if el.hasAttributes() else {}
        print(f"{i}. <{tag}> {attrs} -> '{text}'")


# ==========================================
# 💡 DEMO CHẠY THỬ TẤT CẢ CÁC BÀI
# ==========================================
def main():
    # Bài 2.1
    create_company_xml("company_info.xml", {
        "name": "Nguyen Van A",
        "address": "123 Đường ABC, Hà Nội",
        "phone": "0909123456",
        "tax_id": "0102030405"
    })

    # Bài 2.2
    create_students_xml("students.xml", [
        {"id": "SV001", "name": "Tran Thi B", "year": 2001, "class": "K61CNTT", "gender": "Nữ"},
        {"id": "SV002", "name": "Le Van C", "year": 2000, "class": "K61HTTT", "gender": "Nam"},
        {"id": "SV003", "name": "Pham Van D", "year": 2002, "class": "K61KTMT", "gender": "Nam"}
    ])

    # Bài 2.3
    create_sample_xml("sample.xml")

    # Bài 2.4
    parse_with_minidom("sample.xml")

    # Bài 2.5
    list_elements_by_tagname("sample.xml", "staff")
    list_elements_by_tagname("sample.xml", "name")


if __name__ == "__main__":
    main()
