# 💻 Schedule Management Service Based on Timetable Linkage

This repository contains a prototype of **Schedule Tetris**, a project submitted to the **1st Open Source Software Idea Hackathon Camp**.
<br/>

![Schedule Tetris Presentation Slide](https://github.com/user-attachments/assets/cf9417cc-bc33-4eaf-a9e8-fc92545a8d85)
<br/>
<br/>

## 🕹️ Schedule Tetris

**Schedule Tetris** is a schedule management application that enables users to **quickly and efficiently arrange meetings** by **sharing available time slots** through **timetable synchronization**.
  
Many existing scheduling applications have limitations such as:
- Inability to view other users’ schedules
- Lack of automatic timetable integration
  
To address these issues, Schedule Tetris was designed to **reduce the time spent on schedule-related decision making** by visually combining multiple users’ timetables.
<br/>

![Schedule Tetris Slide 1](https://github.com/user-attachments/assets/b7f786c7-67bf-4533-9114-1425095e98fc)
![Schedule Tetris Slide 2](https://github.com/user-attachments/assets/36714ebd-3eda-45c2-8d94-f421a1646aa8)
<br/>
<br/>

## 📱 Features

### 1. Launching Schedule Tetris

The main screen displays an empty timetable along with the following buttons:
- Oasis Login  
- View My Timetable  
- Load Other Timetables  
- Export Timetable  
<br/>
<br/>

### 2. Oasis Login (Student ID / Password)

When the **Oasis Login** button is clicked, a login window appears. Users enter the same student ID and password used for **OASIS (Jeonbuk National University Portal)**.
    
The following process runs automatically:
  
> Oasis Login → Portal Main Page → Menu Button → One-stop Menu → Student Class Timetable Output → Export to Excel  
  
The exported Excel file containing the user’s class timetable is saved to `C:\Users\{username}\Downloads`. After saving, the browser window closes automatically.
<br/>
<br/>

### 3. Load My Timetable

Clicking **View My Timetable** loads the user’s class timetable from the Excel file into the empty timetable on the main screen.
The timetable is displayed in **30-minute intervals**, matching the format used by the official Oasis system.
<br/>
<br/>

### 4. Load Other Users’ Timetables

Clicking **Load Other Timetables** allows users to select other users’ timetable files from a folder.
  
- Selected timetables are overlaid onto the user’s own timetable  
- Multiple timetables can be layered sequentially  
- The earliest loaded timetable takes priority  
  (later schedules are not displayed if time conflicts occur)
<br/>
<br/>

### 5. Add a New Schedule

Clicking an empty time slot adds a **1-hour schedule block**.
  
- If a schedule already exists afterward, a **30-minute block** is added instead  
- Clicking an existing class schedule displays the message:  
  > “This time slot already contains a class schedule!”
  
No new schedule is added in this case.
<br/>
<br/>

### 6. Delete a Schedule

Newly created schedules can be deleted by clicking on them.

- Clicking the **start time** deletes the schedule in **1-hour units**
- Clicking **30 minutes before the end time** deletes it in **30-minute units**
<br/>
<br/>

### 7. Export Timetable with Added Schedules

Clicking **Export Timetable** saves the timetable—including newly added schedules as an Excel file.
The exported file is stored in the same directory as the Python source code.
<br/>
<br/>

## 💿 Key Files

- `publicCode.py` : Main file that runs the Schedule Tetris program  
- `publicOasis.py` : Contains the Oasis crawling logic used by the main program  
<br/>
<br/>

## ⏰ Notes & Requirements

- Additional directory path configuration is required before execution  
- The program uses **ChromeDriver** - Users must install a ChromeDriver version that matches their local Chrome browser  
  
ChromeDriver can be downloaded from:  
https://github.com/GoogleChromeLabs/chrome-for-testing/blob/main/data/latest-versions-per-milestone-with-downloads.json
<br/>
<br/>

## 🙆🏻‍♀️ Contributors

- 👩‍💻 Developers: **Sehyun Kim**, **Jeongmin Lim**
- 🎨 Designer: **Minkyung Kim**
- 🗓 Development Period: **2023 December 1 – 2023 December 3 (3 days total)**
<br/>
<br/>
