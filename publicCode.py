import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import os
import publicOasis # 로그인 창

# messagebox 표기
def print_Info(messages):
    messagebox.showinfo("안내", messages)

# 약속 이름 상수 선언
ARE_YOU_OKAY_IS_THIS = "약속!"

# 디렉토리 경로 설정, 파일이 저장된 폴더 경로
timeTablefiles = []
def read_files_in_dir():
    global timeTablefiles
    global is_readed
    
    directory_path = '' # 시간표 파일이 있는 폴더 경로로 설정해주세요!
    my_folder_path = '' # 다운로드 폴더 경로를 적어주세요!
    timeTablefiles = [] 
    
    files = os.listdir(my_folder_path)
    files = [f for f in files if f.endswith('.xlsx')]
    
    # 오래된 파일 -> 최신 파일 순으로 정렬
    files.sort(key=lambda x: os.path.getmtime(os.path.join(my_folder_path, x)))
    if files:
        latest_file = files[-1]
        file_path = os.path.join(my_folder_path, latest_file)
        
        excel_file = pd.ExcelFile(file_path)
        df = excel_file.parse(excel_file.sheet_names[0])
        df = df.fillna(' ')
        
        # 내 시간표 먼저 저장
        timeTablefiles.append(df)
    else:
        print_Info("해당 경로에 엑셀 파일이 없습니다.")
        return
    
    is_readed = 1
    
    # 다른 사람 시간표 저장하기
    file_list = os.listdir(directory_path)
    xlsx_files = [file for file in file_list if file.endswith('.xlsx')]
    
    # .xlsx 파일 전체 저장
    for xlsx_file in xlsx_files:
        excel_file_path = directory_path + '\\' + xlsx_file
        df = pd.read_excel(excel_file_path)
        df = df.fillna(' ')
        timeTablefiles.append(df)

is_logined = 0
def is_this_null():
    global is_logined
    if is_logined == 0:
        print_Info("로그인을 진행 후 본인의 시간표를 로드해주세요!")
        return 1
    
    children = tree.get_children()
    if children:
        return 0
    else:
        print_Info("먼저 본인의 시간표를 불러와주세요!")
        return 1

def save_my_timetable():
    global timeTablefiles
    if is_this_null():
        return
    timeTablefiles[0].to_excel('mySchedule.xlsx', index=False)
    print_Info("시간표가 저장되었습니다~!")

# 클릭 이벤트
def on_item_click(event):
    global timeTablefiles
    global mainTimeTable
    
    if is_this_null():
        return
    
    x, y = event.x, event.y

    # 클릭된 위치의 행을 확인
    item_id = tree.identify_row(y)
    
    # 클릭된 위치의 열을 확인
    column_id = tree.identify_column(x)
    column_id = column_id.split("#")[-1]  # 열의 ID에서 순번을 추출
    col_id = int(column_id) - 1
        
    # 현재 행의 인덱스를 얻기
    current_index = tree.index(item_id)
    
    # 다음 행의 item_id 계산
    next_index = current_index + 1
    next_item_id = tree.get_children()[next_index] if next_index < len(tree.get_children()) else None

    if next_item_id:
        next_item_values = list(tree.item(next_item_id, 'values'))

    # 행과 열을 이용하여 데이터를 가져옴
    item_values = list(tree.item(item_id, 'values')) 
    
    # 1시간 단위로 시간대 추가하기
    if(item_values[col_id] == ' '): #빈 시간대
        response = messagebox.askyesno("확인", f"{item_values[1]}에 새 일정을 추가하시겠습니까?")
        if response: # 새로운 스케쥴 표기
            new_value = ARE_YOU_OKAY_IS_THIS
            item_values[col_id] = new_value
            tree.item(item_id, values=item_values)
            
            timeTablefiles[0].loc[current_index][col_id] = new_value # 본래 본인 시간표에 저장
            mainTimeTable.loc[current_index][col_id] = new_value
            
            if next_item_id and (next_item_values[col_id] == ' '):
                new_value = ARE_YOU_OKAY_IS_THIS
                next_item_values[col_id] = new_value
                tree.item(next_item_id, values=next_item_values)
                timeTablefiles[0].loc[next_index][col_id] = new_value
            mainTimeTable.loc[current_index][col_id] = new_value
                
    elif(item_values[col_id] == ARE_YOU_OKAY_IS_THIS): # 스케쥴 삭제
        response = messagebox.askyesno("확인", "삭제하시겠습니까?")
        if response: 
            new_value = ' '
            item_values[col_id] = new_value
            tree.item(item_id, values=item_values)
            timeTablefiles[0].loc[current_index][col_id] = new_value
            mainTimeTable.loc[current_index][col_id] = new_value
            
            if next_item_id and (next_item_values[col_id] == ARE_YOU_OKAY_IS_THIS):
                new_value = ' '
                next_item_values[col_id] = new_value
                tree.item(next_item_id, values=next_item_values)
                timeTablefiles[0].loc[next_index][col_id] = new_value
                mainTimeTable.loc[current_index][col_id] = new_value
    
    else: #수업 있는 시간대
        print_Info("해당 시간대는 불가능합니다.")

def read_excel_data():
    global is_logined
    global is_changed
    global is_readed
    if is_logined == 0:
        print_Info("로그인을 진행 후 본인의 시간표를 로드해주세요!")
        return
    
    #파일 읽기 전에 현재 시간표 저장
    if is_readed != 1:
        read_files_in_dir()
    
    # 트리 초기화
    tree.delete(*tree.get_children())
    global mainTimeTable
    global indexs
    indexs = 1
    
    for i, row in timeTablefiles[0].iterrows():
        tree.insert('', 'end', values=row.tolist())
        mainTimeTable = timeTablefiles[0]

# 다른 사람 파일 읽어오기
def read_other_people():
    global mainTimeTable
    if is_this_null():
        return
    
    df1 = mainTimeTable
    df2 = timeTablefiles[indexs]
    
    mergedata = merge_files(df1, df2)
    change_files(mergedata)
    
    tree.delete(*tree.get_children())
    
    for i, row in mergedata.iterrows():
        tree.insert('', 'end', values=row.tolist())
    
def change_files(data):
    global mainTimeTable
    global indexs
    
    mainTimeTable = data
    indexs += 1
    
    # out of index 방지
    if(indexs == len(timeTablefiles)):
        indexs -= 1
        print_Info("모든 시간표 파일을 다 합쳤습니다.")
        return
    
    
def merge_files(df1, df2):
    df1 = df1.fillna(' ')
    df2 = df2.fillna(' ')

    resultTime = []
    conflictTime = []
    dic = {}
    for col in (df1.columns):
        temp = []
        for i in range(len(df1[col])):
            result = df1[col][i] if df1[col][i] != ' ' else df2[col][i] #약속 자동 지워지게, df처리
            if result == ARE_YOU_OKAY_IS_THIS:
                if df2[col][i] != ' ':
                    result = df2[col][i] #약속 시간과 타인의 수업 스케쥴 충돌시 후자 우선
                    conflictTime.append(df2['(시간)'][i]) #충돌 시간대 저장
                    
            temp.append(result)
        resultTime.append(temp)
        dic[col] = temp
        
    if conflictTime:
        infoConf = str(conflictTime) + "의 시간대와 충돌이 발생해요~!"
        print_Info(infoConf)

    mergedata = pd.DataFrame(dic)
    return mergedata
    
def update_my_schdue():
    global is_logined
    global is_readed
    
    if is_readed:
        print_Info("이미 로그인을 완료하였습니다~!")
        return
        
    is_logined = 1
    publicOasis.main() # 로그인 창만 키고 실제로 로그인 안했을 시 문제 발생

is_readed = 0

# Tkinter 창 생성
root = tk.Tk()
root.title("일정 테트리스")

# Treeview 생성 (표 형식의 위젯)
tree = ttk.Treeview(root, columns=list(range(8)), show='headings', height=15)

# Treeview의 열 제목 설정
titleData = ['시간표', '시간', '월', '화', '수', '목', '금', '토']
for i in range(8):
    tree.heading(i, text = titleData[i])

# Treeview의 각 열의 너비 설정
for i in range(8):
    tree.column(i, width=100)

# 수직 스크롤바 추가
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

# 행, 열 클릭 시 처리
tree.bind("<ButtonRelease-1>", on_item_click)

# 데이터 불러오기 버튼 생성
button = tk.Button(root, text="내 시간표 보기", command=read_excel_data)
button2 = tk.Button(root, text="다른 사람 시간표 불러오기", command=read_other_people)
button3 = tk.Button(root, text="시간표 내보내기", command=save_my_timetable)
button4 = tk.Button(root, text="오아시스 로그인", command=update_my_schdue)

# Treeview와 버튼을 화면에 배치
tree.pack(pady=10)
button3.pack(side=tk.RIGHT, padx=5)
button2.pack(side=tk.RIGHT, padx=5)
button.pack(side=tk.RIGHT, padx=5)
button4.pack(side=tk.RIGHT, padx=5)

# Tkinter 메인 루프 시작 
root.mainloop()
