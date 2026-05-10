from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('departments', DepartmentViewSet)
router.register('courses', CourseViewSet)
router.register('subjects', SubjectViewSet)
router.register('students', StudentViewSet)
router.register('faculty', FacultyViewSet)
router.register('faculty-subjects', FacultySubjectViewSet)
router.register('attendance', AttendanceViewSet)
router.register('fees-structure', FeeStructureViewSet)
router.register('fees-payment', FeePaymentViewSet)
router.register('exams', ExamViewSet)
router.register('results', ResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]