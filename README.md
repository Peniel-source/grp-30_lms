
    Project Overview

This project is a command line Learning Management System (LMS) created in Python with a MySQL database. The system has three different user accounts—students, instructors, and admins—all with different functions. Users can create an account, sign in, and begin using users will be provided options based on the user role selected. The LMS supports features such as course tracking, academic progress, disciplinary, transcript requests, etc.
   
   
   
   Role Based Features:
   
    Students: Students login with email that ends with @alustudent.com and be able to:
1. View Courses
2. Check Academic Progress
3. Check Financial Standing
4. Disciplinary Standing
Enter your choice (1–5):  
    Instructors
   
    Instructors: Login with the email that ends with @alueducation.com and be able:
    What would you like to do?:
-------------------------
1. Check Instructed Courses
2. Create Assignments
3. Check Attendance
4. Check Student Records
5. Update Academic status
Enter your choice (1–5):

    For admins:
   
    Admins: Login with email that ends with @aluadmin.com and be able to:
1. Manage Students
2. Assign Instructor
3. Issue Transcripts
4. Generate Report
5. View Signup Requests
Enter your choice (1–6):


Steps to run the project:
1) Clone repo:
    git clone <repo_url>
    cd <repo_directory>
 2) Installing libraries:
      pip install mysql-connector-python bcrypt
3) Set up data base:
   MySQL server is accessible with the connection details in db.py
4) Run app:
   python3 main.py
5) Authentication:
     sign up: if you are first time user
     Login: if you are already signed up

├── db.py                      
├── main.py                   
├── menus.py                 
├── tables.py                 
├── academic_progress.py      
├── assign_instructor.py      
├── create_assignments.py                      
├── manage_people.py                
├── update_progress.py       
├── view_courses.py           
├── disciplinary_standing.py 
├── financial_standing.py     
├── signup_approval.py  


Requirements:
  Python 3.x
  mysql-connector-python
  bcrypt

    Contributers:

    1. Peniel Nissi Obeng
    2. Natinael Boda Borana
    3. Esther Kirabo
    4. Kenia Umutoni


