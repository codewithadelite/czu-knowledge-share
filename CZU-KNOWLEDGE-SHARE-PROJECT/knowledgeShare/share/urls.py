"""Web application urls endpoints for all czu knowledge share pages
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('userLogin/', views.user_login, name='user_login'),
    path('auth_failed/', views.auth_failed, name='auth_failed'),
    path('logout/', views.logout_user, name='logout'),

    path('administrator/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('administrator/view-subjects/', views.view_subjects, name='view_subjects'),
    path('administrator/add-subject/', views.add_subject, name='add_subject'),
    path('administrator/update-subject/<int:pk>/', views.update_subject, name='update_subject'),
    path('administrator/subject/<int:pk>/status', views.change_subject_status, name='change_subject_status'),

    path('administrator/view-faculty/', views.view_faculty, name='view_faculty'),
    path('administrator/add-faculty/', views.add_faculty, name='add_faculty'),
    path('administrator/update-faculty/<int:pk>/', views.update_faculty, name='update_faculty'),

    path('administrator/view-study-type/', views.view_study_type, name='view_study_type'),
    path('administrator/add-study-type/', views.add_study_type, name='add_study_type'),
    path('administrator/update-study-type/<int:pk>/', views.update_study_type, name='update_study_type'),
    path('administrator/task/', views.task, name='task'),
    path('administrator/task-status/<int:pk>/', views.task_status, name='task_status'),

    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/shared-files/', views.shared_files, name='shared_files'),
    path('student/file-details/<int:pk>/', views.file_details, name='file_details'),
    path('student/files-found/', views.search_files, name='search_files'),
    path('student/my-files/', views.my_files, name='my_files'),
    path('student/file-status/<int:pk>', views.file_status, name='file_status'),
    path('student/add-file/', views.add_file, name='add_file'),
    path('student/update-file/<int:pk>', views.update_file, name='update_file'),
    path('student/received-request/', views.received_request, name='received_request'),
    path('student/request-approve/<int:pk>', views.request_approve, name='request_approve'),
    path('student/request-reject/<int:pk>', views.request_reject, name='request_reject'),
    path('student/sent-request/', views.sent_request, name='sent_request'),
    path('student/request-cancel/<int:pk>', views.request_cancel, name='request_cancel'),
    path('student/send-request/<int:pk>', views.send_request, name='send_request'),
    path('student/save-comment/', views.save_comment, name='save_comment'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)