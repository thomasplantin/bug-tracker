# Bug Tracker

## Software Requirements Specifications (SRS):

---

<br>

### Introduction

---

The goal of this project is to create a bug tracking system that developers can use to specify issues or defects with a certain piece of software. These issues are reported by submitting a ticket. Each ticket has an author, a person or more assigned, a ticket number, a title, a description, a date of submission, a deadline, a priority level, and a current state (open, closed, or under development).

<br>

### Specifications:

---

**Users**:

    - First Name
    - Last Name
    - User ID

**Tickets**:

    - Title
    - Description
    - Ticket Number
    - Author
    - Assignee(s)
    - Submission Date
    - Deadline
    - Priority Level (Low, Medium, High)
    - Current State (Open, Closed, Under Development)

<br>

### Technical Tools

---

**Front-end development:** HTML, CSS, Jquery, Javascript.

**Back-end development:** Django, Python, MySQL (AWS RDS).

<br>

### Scheduling:

---

| **Milestone** |                   **Description**                   |
|:-------------:|:---------------------------------------------------:|
|       1       | Back-end: Database + API                            |
|       2       | Front-end: Application Design                       |
|       3       | Front-end & Back-end: Integrating Views and Designs |

<br>
<br>

### Instructions
---
**Installing requirements.txt file inside virtual env with Python:**

1 - Go to your project's root directory (bug-tracker)

    cd /Path/to/project/root/bug-tracker

2 - Create your virtual env (one of the two following ways):

        - if `python -V` gives Python3, then run `virtualenv .`
        - if `python -V` gives Python2, then run `virtualenv -p python3 .`

3 - Activate the environment

    source bin/activate

4 - Install the requirements 
    
    pip3 install -r requirements.txt

<br>

---

**Connecting to MySQL DB with Django:**

1 - In `settings.py`, replace the database configuration code:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_name',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'DB_user',
            'PASSWORD': 'DB_password',
        }
    }

2 - Make the migrations:

    python manage.py makemigrations 
    python manage.py migrate
