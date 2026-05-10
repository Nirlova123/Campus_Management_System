from django.contrib import admin
from .models import (
    User,
    Department,
    Course,
    Subject,
    Student,
    Faculty,
    FacultySubject,
    Attendance,
    FeeStructure,
    FeePayment,
    Exam,
    Result
)

# ================= USER =================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
        'role',
        'phone',
        'is_staff',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
    )

    search_fields = (
        'username',
        'email',
    )


# ================= DEPARTMENT =================
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
    )

    search_fields = (
        'name',
        'code',
    )


# ================= COURSE =================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
        'department',
        'duration_years',
    )

    list_filter = (
        'department',
    )

    search_fields = (
        'name',
        'code',
    )


# ================= SUBJECT =================
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
        'course',
        'semester',
    )

    list_filter = (
        'course',
        'semester',
    )

    search_fields = (
        'name',
        'code',
    )


# ================= STUDENT =================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'enrollment_number',
        'course',
        'semester',
        'admission_date',
    )

    list_filter = (
        'course',
        'semester',
    )

    search_fields = (
        'enrollment_number',
        'user__username',
    )


# ================= FACULTY =================
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'employee_id',
        'department',
        'designation',
    )

    list_filter = (
        'department',
    )

    search_fields = (
        'employee_id',
        'user__username',
    )


# ================= FACULTY SUBJECT =================
@admin.register(FacultySubject)
class FacultySubjectAdmin(admin.ModelAdmin):

    list_display = (
        'faculty',
        'subject',
    )

    list_filter = (
        'subject',
    )


# ================= ATTENDANCE =================
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'subject',
        'date',
        'status',
    )

    list_filter = (
        'date',
        'subject',
        'status',
    )

    search_fields = (
        'student__user__username',
    )


# ================= FEE STRUCTURE =================
@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):

    list_display = (
        'course',
        'semester',
        'amount',
    )

    list_filter = (
        'course',
        'semester',
    )


# ================= FEE PAYMENT =================
@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'fee_structure',
        'amount_paid',
        'payment_date',
        'transaction_id',
    )

    search_fields = (
        'transaction_id',
    )


# ================= EXAM =================
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'subject',
        'date',
        'total_marks',
    )

    list_filter = (
        'subject',
    )


# ================= RESULT =================
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'exam',
        'marks_obtained',
    )

    list_filter = (
        'exam',
    )