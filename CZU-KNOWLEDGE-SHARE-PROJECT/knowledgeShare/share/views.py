from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import (
    User,
    Administrator,
    Student,
    Faculty,
    StudyType,
    StaffCategory,
    Subject,
    File,
    FilePermission,
    Comment,
    Task,
)

from .decorators import admin_verification, student_verification
from .forms import SubjectForm, FacultyForm, StudyTypeForm, FileForm


def index(request):
    """
    Function for homepage rendering
    """

    return render(request, "share/index.html")


def user_login(request):
    """
    Function for logging in users
        : If logged in user is admin, will be redirected to ADMIN DASHBOARD
        : If logged in user is student, will be redirected to STUDENT DASHBOARD
    """

    context = {}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_admin == True:
                return redirect(reverse("admin_dashboard"))
            return redirect(reverse("student_dashboard"))
        context["messages"] = [
            "Username or password is incorrect",
        ]
    return render(request, "share/userLogin.html", context)


@login_required(login_url="user_login")
def logout_user(request):
    """
    Function to logout user and destroy session
    """

    logout(request)
    return redirect(reverse("user_login"))


"""----------------------------------ADMINISTRATION SECTION--------------------------"""


@admin_verification
@login_required(login_url="user_login")
def admin_dashboard(request):
    """
    Function for admin dashboard, This function query total records in the database
    for subjects, files, faculties......... to be displayed on the User Inreface
    """

    total_students = Student.objects.all().count()
    total_files = File.objects.all().count()
    total_subjects = Subject.objects.all().count()
    total_faculties = Faculty.objects.all().count()
    total_staff = StaffCategory.objects.all().count()
    total_studies_type = StudyType.objects.all().count()
    task_pending_total = Task.objects.filter(user=request.user, is_done=False).count()

    context = {
        "total_students": total_students,
        "total_files": total_files,
        "total_subjects": total_subjects,
        "total_faculties": total_faculties,
        "total_staff": total_staff,
        "total_studies_type": total_studies_type,
        "task_pending_total": task_pending_total,
    }

    return render(request, "share/admin/dashboard.html", context)


@login_required(login_url="user_login")
@admin_verification
def view_subjects(request):
    """
    Function to query all registered subjects in database and pass them to html interface
    """

    subjects = Subject.objects.all().order_by("-id")
    context = {"subjects": subjects}
    return render(request, "share/admin/view-subjects.html", context)


@login_required(login_url="user_login")
@admin_verification
def add_subject(request):
    """
    Function to add new subject in database.
    """

    form = SubjectForm
    context = {"form": form}

    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_subject = form.save(commit=False)
            new_subject.status = 1
            new_subject.save()
            messages.success(request, "Subject added successfully")
        else:
            print(form.errors)
            messages.warning(request, form.errors)
    return render(request, "share/admin/add-subject.html", context)


@login_required(login_url="user_login")
@admin_verification
def update_subject(request, pk):
    """
    Function to update specific subject in database.
    """

    obj = get_object_or_404(Subject, id=pk)
    form = SubjectForm(instance=obj)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully")
            form = SubjectForm(request.POST)
        else:
            messages.warning(request, "Failed to update subject, try again")

    context = {"form": form}

    return render(request, "share/admin/update-subject.html", context)


@login_required(login_url="user_login")
@admin_verification
def change_subject_status(request, pk):
    """
    Function to change subject status.
    : 1 -> Set it to 1 to activate it.
    : 2 -> Set it to 2 to deactivate it.
    """

    obj = get_object_or_404(Subject, id=pk)
    obj.status = 2 if obj.status == 1 else 1
    obj.save()

    return redirect(reverse("view_subjects"))


@login_required(login_url="user_login")
@admin_verification
def view_faculty(request):
    """
    Function to query all registered faculties in database and pass them to html interface.
    """

    faculties = Faculty.objects.all().order_by("-id")
    context = {"faculties": faculties}
    return render(request, "share/admin/view-faculty.html", context)


@login_required(login_url="user_login")
@admin_verification
def add_faculty(request):
    """
    Function to add new faculty in database.
    """

    form = FacultyForm
    context = {"form": form}

    if request.method == "POST":
        form = FacultyForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty added successfully")
        else:
            messages.warning(request, " Failed to add faculty, Try again")
    return render(request, "share/admin/add-faculty.html", context)


@login_required(login_url="user_login")
@admin_verification
def update_faculty(request, pk):
    """
    Function to update specific faculty in database.
    """

    obj = get_object_or_404(Faculty, id=pk)
    form = FacultyForm(instance=obj)

    if request.method == "POST":
        form = FacultyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty updated successfully")
            form = FacultyForm(request.POST)
        else:
            messages.warning(request, "Failed to update faculty, try again")

    context = {"form": form}

    return render(request, "share/admin/update-faculty.html", context)


@login_required(login_url="user_login")
@admin_verification
def view_study_type(request):
    """
    Function to query all registered studyTypes in database and pass them to html interface
    """

    study_types = StudyType.objects.all().order_by("name")
    context = {"study_types": study_types}
    return render(request, "share/admin/view-study-type.html", context)


@login_required(login_url="user_login")
@admin_verification
def add_study_type(request):
    """
    Function to add new studyType in database.
    """

    form = StudyTypeForm
    context = {"form": form}

    if request.method == "POST":
        form = StudyTypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Study type added successfully")
        else:
            messages.warning(request, " Failed to add study type, Try again")
    return render(request, "share/admin/add-study-type.html", context)


@login_required(login_url="user_login")
@admin_verification
def update_study_type(request, pk):
    """
    Function to update specific studyType.
    """

    obj = get_object_or_404(StudyType, id=pk)
    form = StudyTypeForm(instance=obj)

    if request.method == "POST":
        form = StudyTypeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Study type updated successfully")
            form = StudyTypeForm(request.POST)
        else:
            messages.warning(request, "Failed to update study type, try again")

    context = {"form": form}

    return render(request, "share/admin/update-faculty.html", context)


@login_required(login_url="user_login")
@admin_verification
def task(request):
    """
    Function to query all tasks assigned to admin user who is logged In.
    """

    tasks = Task.objects.filter(user=request.user).order_by("-id")
    context = {"tasks": tasks}

    return render(request, "share/admin/task.html", context)


@login_required(login_url="user_login")
@admin_verification
def task_status(request, pk):
    """
    Function to change task is_done status.
    : True -> Set task to DONE status.
    : False -> Set task to PENDING status.
    """

    obj = get_object_or_404(Task, id=pk)
    obj.is_done = True if obj.is_done == False else False
    obj.save()

    return redirect(reverse("task"))


"""----------------------------------END OF ADMINISTRATION SECTION--------------------------"""


"""----------------------------------STUDENTS SECTION--------------------------"""


@student_verification
@login_required(login_url="user_login")
def student_dashboard(request):
    """
    Function for student dashboard, This function query total records in the database
    for files, requested_files,approved_files to be displayed on the student admin Interface
    """

    total_files = File.objects.filter(user=request.user).count()

    total_files_permission_request = FilePermission.objects.filter(
        file_link__user=request.user
    ).count()

    total_files_permission_approved = FilePermission.objects.filter(
        file_link__user=request.user, status=1
    ).count()

    context = {
        "total_files": total_files,
        "total_files_permission_request": total_files_permission_request,
        "total_files_permission_approved": total_files_permission_approved,
    }

    return render(request, "share/students/dashboard.html", context)


@student_verification
@login_required(login_url="user_login")
def add_file(request):
    """
    Function to add new file in the system.
    """

    form = FileForm()

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            messages.success(request, "File Added Successfully")
        else:
            messages.success(request, "Failed Try again")
    context = {"form": form}
    return render(request, "share/students/add-file.html", context)


@student_verification
@login_required(login_url="user_login")
def update_file(request, pk):
    """
    Function for updating specific file.
    """

    obj = get_object_or_404(File, id=pk)
    form = FileForm(instance=obj)

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            messages.success(request, "File Updated Successfully")
        else:
            messages.success(request, "Failed To update file Try again")
    context = {"form": form}
    return render(request, "share/students/update-file.html", context)


@student_verification
@login_required(login_url="user_login")
def shared_files(request):
    """
    Function to query all shared files that are in database wirth limit of 12.
    """

    files = File.objects.all().order_by("-id")[:12]

    context = {"files": files}
    return render(request, "share/students/shared-files.html", context)


@student_verification
@login_required(login_url="user_login")
def file_details(request, pk):
    """
    Function for selecting details for specific file.
        :Viewing details of file is only allowed
            -If file is uploaded by logged In  user. OR
            -If file is set to public. OR
            -If logged In user is granted permission by the owner of the file
    """

    file = get_object_or_404(File, id=pk)
    file_comments = Comment.objects.filter(file_link=file)

    view_allowed = False

    file_requests = FilePermission.objects.filter(file_link=file)
    permitted_users = [user.requester.id for user in file_requests if user.status == 1]

    if file.user == request.user:
        view_allowed = True
    elif file.is_public:
        view_allowed = True
    elif request.user.id in permitted_users:
        view_allowed = True

    context = {
        "view_allowed": view_allowed,
        "file": file,
        "file_comments": file_comments,
    }
    return render(request, "share/students/file-details.html", context)


@student_verification
@login_required(login_url="user_login")
def save_comment(request):
    """
    Function for saving comment for specific file.
    """

    if request.method == "POST":
        file = get_object_or_404(File, id=request.POST.get("file_id"))
        message = request.POST.get("message")

        comment = Comment(comment=message, user=request.user, file_link=file)
        comment.save()
    return redirect(reverse("file_details", args=(request.POST.get("file_id"),)))


@student_verification
@login_required(login_url="user_login")
def search_files(request):
    """
    Function to search file that has title OR description OR subject
    that contains passed keyword by the user.
    """

    if request.method == "GET":
        q = request.GET.get("q")

        files_found = File.objects.filter(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(subject__subject_code__icontains=q)
            | Q(subject__name__icontains=q)
        )

        total_found = files_found.count()
    context = {"files_found": files_found, "total_found": total_found}
    return render(request, "share/students/files-found.html", context)


@student_verification
@login_required(login_url="user_login")
def my_files(request):
    """
    Function to query files that belongs to logged In user.
    """

    files = File.objects.filter(user=request.user).order_by("-id")
    context = {"files": files}
    return render(request, "share/students/my-files.html", context)


@student_verification
@login_required(login_url="user_login")
def file_status(request, pk):
    """
    Function to change status of the file
        :True -> Setting file to public.
        :False -> Setting file to private.
    """

    file = get_object_or_404(File, id=pk)
    if file.user == request.user:
        if file.is_public:
            file.is_public = False
        else:
            file.is_public = True
        file.save()
    else:
        return HttpResponse(
            "Failed, You cant change status to file that doesnt belong to you"
        )
    return redirect(reverse("my_files"))


@student_verification
@login_required(login_url="user_login")
def received_request(request):
    """
    Function to query received request for current logged In student.
    """

    requests = FilePermission.objects.filter(file_link__user=request.user).order_by(
        "-id"
    )
    context = {"requests": requests}
    return render(request, "share/students/received-requests.html", context)


@student_verification
@login_required(login_url="user_login")
def sent_request(request):
    """
    Function to query request that have been sent by the current
    logged in student.
    """

    requests = FilePermission.objects.filter(requester=request.user).order_by("-id")
    totatal_requests = requests.count()
    context = {"requests": requests, "total_requests": totatal_requests}
    return render(request, "share/students/sent-request.html", context)


@student_verification
@login_required(login_url="user_login")
def request_approve(request, pk):
    """
    Function to approve request for specific file and specific student.
    """

    requested = get_object_or_404(FilePermission, id=pk)

    if requested.file_link.user == request.user:
        requested.status = 1  # It means setting status to approved
        requested.save()
    else:
        return HttpResponse("You cant approve request that doesnt belong to you. ")

    return redirect(reverse("received_request"))


@student_verification
@login_required(login_url="user_login")
def request_cancel(request, pk):
    """
    Function to cancel request.
    """

    requested = get_object_or_404(FilePermission, id=pk)

    """
    Canceling request
    """

    if requested.requester == request.user:
        requested.delete()
    else:
        return HttpResponse(
            "You cant cancel  request that have not been requested by you. "
        )

    return redirect(reverse("sent_request"))


@student_verification
@login_required(login_url="user_login")
def send_request(request, pk):
    """
    Function to send permission request to the owner of the file for the
    specific file.
    """

    file = get_object_or_404(File, id=pk)

    if not file.is_public:
        if not file.user == request.user:
            permission = FilePermission(
                requester=request.user, file_link=file, owner=file.user
            )
            permission.save()

            return redirect(reverse("sent_request"))
        else:
            return HttpResponse("You dont have to request for your own files")
    else:
        return HttpResponse("You dont have to request for public files")
    return redirect(reverse("sent_request"))


@student_verification
@login_required(login_url="user_login")
def request_reject(request, pk):
    """
    Function to reject request for specific file.
    """

    requested = get_object_or_404(FilePermission, id=pk)

    if requested.file_link.user == request.user:
        requested.status = 2  # It means setting status to rejected
        requested.save()
    else:
        return HttpResponse("You cant reject request that doesnt belong to you. ")

    return redirect(reverse("received_request"))


def auth_failed(request):
    """
    Function to send HttpResponse message that user is not authorized for some thing.
    """

    context = {}
    return HttpResponse(f"Not authenticated")
