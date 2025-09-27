# Copilot Instructions for This Codebase

## Overview
This project contains Python code for solving introductory programming exercises, organized as Jupyter notebooks. The main focus is on object-oriented programming and basic data processing, with each exercise typically implemented as a class and demonstrated with example usage.

## Structure
- All code is in Jupyter notebooks, currently in `chuong 1/baitap.ipynb`.
- Each exercise is separated by markdown headings and code cells.
- Example classes: `HinhChuNhat` (rectangle), `ThiSinh` (student/candidate).

## Patterns & Conventions
- Each class encapsulates both data and display logic (e.g., `hien_thi()` prints all relevant info).
- Vietnamese is used for variable, class, and method names, as well as for output and comments.
- Exercises are labeled in markdown and code output (e.g., `BÀI 1`, `BÀI 2`).
- Data is hardcoded for demonstration; no user input or file I/O is present.

## Developer Workflow
- Edit and run code directly in the notebook (`baitap.ipynb`).
- Add new exercises as new code/markdown cells, following the existing pattern.
- No build or test scripts; results are visible via notebook output.

## Key Files
- `chuong 1/baitap.ipynb`: Main notebook with all exercises and solutions.

## Example Pattern
```python
class HinhChuNhat:
    def __init__(self, dai=0, rong=0):
        self.dai = dai
        self.rong = rong
    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)
    def tinh_dien_tich(self):
        return self.dai * self.rong
    def hien_thi(self):
        print(f"Chiều dài: {self.dai}")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
```

## Guidance for AI Agents
- Use Vietnamese for all code, comments, and output.
- Follow the class-based structure for each exercise.
- Add new exercises as new cells, clearly labeled in markdown.
- No need for test automation or CI/CD; focus on clarity and correctness in notebook output.
