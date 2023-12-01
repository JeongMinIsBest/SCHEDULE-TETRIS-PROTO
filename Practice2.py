import pandas as pd
import tkinter as tk
from tkinter import ttk

def read_excel_data():
    # 엑셀 파일 경로
    excel_file_path = "C:\\Users\\ljm16\\Downloads\\1701459266896.xlsx"

    # 엑셀 파일에서 데이터를 읽어옴
    df = pd.read_excel(excel_file_path)

    # 데이터프레임을 사용하여 Tkinter의 Treeview에 데이터 추가
    for i, row in df.iterrows():
        tree.insert('', 'end', values=row.tolist())

# Tkinter 창 생성
root = tk.Tk()
root.title("Excel 데이터 불러오기")

# Treeview 생성 (표 형식의 위젯)
tree = ttk.Treeview(root, columns=list(range(8)), show='headings', height=15)

# Treeview의 열 제목 설정
for i in range(8):
    tree.heading(i, text=f'열 {i+1}')

# Treeview의 각 열의 너비 설정
for i in range(8):
    tree.column(i, width=100)

# 수직 스크롤바 추가
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

# 데이터 불러오기 버튼 생성
button = tk.Button(root, text="데이터 불러오기", command=read_excel_data)

# Treeview와 버튼을 화면에 배치
tree.pack(pady=10)
button.pack()

# Tkinter 메인 루프 시작 
root.mainloop()
