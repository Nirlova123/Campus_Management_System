# 🎓 Campus Management System

A modern Full-Stack Campus Management System built using React, Django REST Framework, and PostgreSQL to streamline academic and administrative operations for educational institutions such as colleges, universities, schools, and training centers.

The platform centralizes student, faculty, department, course, subject, attendance, result, and institutional data management through a secure and scalable web application.

---

## 🚀 Overview

Managing educational institutions manually often leads to inefficiencies, data redundancy, and administrative overhead. The Campus Management System addresses these challenges by providing a centralized digital platform for academic and administrative management.

This project demonstrates:

✔ Full-Stack Web Development

✔ RESTful API Design

✔ Role-Based Access Control

✔ Database Modeling & Relationships

✔ Secure Authentication & Authorization

✔ Responsive User Interface

✔ Scalable Architecture

✔ Real-World Institution Management Workflow

---

# ✨ Key Features

## 👨‍🎓 Student Management

* Student Registration
* Student Profile Management
* Student Academic Records
* Department-wise Student Listing
* Course Enrollment Tracking

## 👨‍🏫 Faculty Management

* Faculty Registration
* Faculty Profile Management
* Department Assignment
* Subject Allocation

## 🏢 Department Management

* Create Departments
* Update Department Details
* Department-wise Resource Management

## 📚 Course Management

* Course Creation
* Course Assignment
* Course Information Management

## 📖 Subject Management

* Subject Registration
* Subject Allocation
* Department-wise Subject Organization

## 📝 Attendance Management

* Record Student Attendance
* Attendance Monitoring
* Attendance Reports

## 📊 Result Management

* Student Marks Entry
* Result Generation
* Academic Performance Tracking

## 🔐 Authentication & Authorization

* Secure Login System
* Role-Based Access Control
* Admin Access
* Faculty Access
* Student Access

## 📱 Responsive User Interface

* Mobile Friendly
* Tablet Compatible
* Desktop Optimized

---

# 🏗 System Architecture

```text
┌─────────────────────┐
│     React Frontend  │
└──────────┬──────────┘
           │ REST API Calls
           ▼
┌─────────────────────┐
│ Django REST API     │
│ Business Logic      │
│ Authentication      │
└──────────┬──────────┘
           │ ORM
           ▼
┌─────────────────────┐
│ PostgreSQL Database │
└─────────────────────┘
```

---

# 🛠 Technology Stack

## Frontend

* React.js
* JavaScript (ES6+)
* HTML5
* CSS3
* Axios
* React Router

## Backend

* Django
* Django REST Framework (DRF)
* Python

## Database

* PostgreSQL

## Authentication

* Django Authentication System
* JWT Authentication (if implemented)

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
Campus_Management_System/
│
├── backend/
│   ├── core/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── routes/
│   │   └── App.js
│   │
│   └── package.json
│
└── README.md
```

---

# 🗄 Database Design

The system is designed using a relational database model.

### Core Entities

* User
* Student
* Faculty
* Department
* Course
* Subject
* Attendance
* Result

### Relationships

```text
Department
│
├── Students
├── Faculty
├── Courses
└── Subjects

Student
│
├── Attendance
└── Results

Faculty
│
└── Subjects
```

---

# 🔗 REST API Endpoints

## Authentication

```http
POST /api/login/
POST /api/logout/
```

## Students

```http
GET    /api/students/
POST   /api/students/
GET    /api/students/{id}/
PUT    /api/students/{id}/
DELETE /api/students/{id}/
```

## Faculty

```http
GET    /api/faculty/
POST   /api/faculty/
GET    /api/faculty/{id}/
PUT    /api/faculty/{id}/
DELETE /api/faculty/{id}/
```

## Departments

```http
GET    /api/departments/
POST   /api/departments/
```

## Courses

```http
GET    /api/courses/
POST   /api/courses/
```

## Subjects

```http
GET    /api/subjects/
POST   /api/subjects/
```

## Attendance

```http
GET    /api/attendance/
POST   /api/attendance/
```

## Results

```http
GET    /api/results/
POST   /api/results/
```

---

# ⚙ Installation Guide

## Prerequisites

* Python 3.11+
* PostgreSQL
* Node.js 18+
* npm

---

## Clone Repository

```bash
git clone https://github.com/Nirlova123/Campus_Management_System.git

cd Campus_Management_System
```

---

## Backend Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update PostgreSQL credentials in:

```python
settings.py
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Backend Server

```bash
python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Navigate to frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

# 🔒 Security Features

* Authentication-Based Access
* Role-Based Authorization
* Input Validation
* API Data Validation
* Secure Password Storage
* CSRF Protection
* SQL Injection Prevention via Django ORM

---

# 📈 Future Enhancements

* Email Notification System
* Fee Management Module
* Library Management Module
* Online Examination System
* Assignment Submission Portal
* Student Performance Analytics
* Dashboard Charts & Reports
* Multi-Institution Support
* Cloud Deployment
* Docker Containerization

---

# 🧪 Testing

```bash
python manage.py test
```

---

# 🚀 Deployment

The project can be deployed using:

### Frontend

* Vercel
* Netlify

### Backend

* Render
* Railway
* AWS
* DigitalOcean

### Database

* PostgreSQL
* AWS RDS

---

# 👨‍💻 Author

Nirlova Panda

GitHub:
https://github.com/Nirlova123

---

# 📄 License

This project is developed for educational and portfolio purposes.

Feel free to fork, modify, and contribute.
