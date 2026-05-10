from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# =========================================
# CUSTOM USER MODEL
# =========================================
class User(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('FACULTY', 'Faculty'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='STUDENT'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


# =========================================
# DEPARTMENT
# =========================================
class Department(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return self.name


# =========================================
# COURSE
# =========================================
class Course(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=10)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    duration_years = models.IntegerField(default=4)

    def __str__(self):
        return self.name


# =========================================
# SUBJECT
# =========================================
class Subject(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=10)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    semester = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - Semester {self.semester}"


# =========================================
# STUDENT
# =========================================
class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    enrollment_number = models.CharField(
        max_length=20,
        unique=True
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    semester = models.IntegerField(default=1)

    admission_date = models.DateField(
         default=date.today
    )

    def __str__(self):
        return self.user.username


# =========================================
# FACULTY
# =========================================
class Faculty(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='faculty_profile'
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# =========================================
# FACULTY SUBJECT ASSIGNMENT
# =========================================
class FacultySubject(models.Model):

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('faculty', 'subject')

    def __str__(self):
        return f"{self.faculty} -> {self.subject}"


# =========================================
# ATTENDANCE
# =========================================
class Attendance(models.Model):

    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PRESENT'
    )

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        return f"{self.student} - {self.status}"


# =========================================
# FEE STRUCTURE
# =========================================
class FeeStructure(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    semester = models.IntegerField(default=1)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        unique_together = ('course', 'semester')

    def __str__(self):
        return f"{self.course} - Sem {self.semester}"


# =========================================
# FEE PAYMENT
# =========================================
class FeePayment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    fee_structure = models.ForeignKey(
        FeeStructure,
        on_delete=models.CASCADE
    )

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField(
        default=date.today
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return f"{self.student} - {self.amount_paid}"


# =========================================
# EXAM
# =========================================
class Exam(models.Model):

    name = models.CharField(max_length=100)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return self.name


# =========================================
# RESULT
# =========================================
class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    marks_obtained = models.FloatField()

    class Meta:
        unique_together = ('student', 'exam')

    def __str__(self):
        return f"{self.student} - {self.marks_obtained}"