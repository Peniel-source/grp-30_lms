     Project Overview
   This is Learning Management System done built in Python and MYSQL RDBMS. This CLI(Command Line Interface) based app allows users to create the account with the full name, email and password. The users are students, instructors and admin. The app has features like coursetracking, academic progress, viewing financial, desciplinary standing, and much more.
       Features by role
       Students:
The student should login with @alustudent.com email. Then be able to:
1. View Courses
2. Check Academic Progress
3. Check Financial Standing
4. Disciplinary Standing
5. Request for Transcripts
  
  
  Instructors:
Are supposed to login with @alueducation.com email. Then, they will be able to:
1. Check Instructed Courses
2. Create Assignments
3. Check Attendance
4. Check Student Records
5. Update Academic status
    
    
    Admins
Are supposed to login with @aluadmin.com email.
Then, they will be able to:
1. Manage Students
2. Assign Instructor
3. Issue Transcripts
4. Generate Report
5. View Signup Requests
6. Add courses
       
       
        How to run the project?
git clone <repo_url>
cd <repo_directory>


Install required libraries. The program needs mysql.connector and bcrypt
 To install the libraries, run the following command in Command Propmt or other linux terminal
        pip install mysql-connector-python bcrypt


Set up data base:
  Make sure your MySQL server is accessible with the connection details in db.py 
  run the application:
     python3 main.py


Authentication Logic:
   sign up:
   New users should sign up using their email, full name and password.
   Login:
      input email and password you provided during sign up
      the role is determined based on emails domain name. For example, @alustudent.com(student), @alueducation.com(instructor), @aluadmin.com(admin).



Project structure:
├── db.py                      
├── main.py                   
├── menus.py                  
├── tables.py                 
├── academic_progress.py      
├── assign_instructor.py      
├── create_assignments.py                
├── manage_people.py              
├── view_courses.py           
├── disciplinary_status.py 
├── financial_standing.py     
├── signup_approval.py        



Essentials:
  Python 3.x
  mysql-connector-python
  bcrypt



Contributes:
    Group 30-Group Coding lab contributers.
    1. Peniel Nissi Obeng
    2.Ester Kirabo
    3.Natinael Boda Borana
    4.Kenia Umutoni