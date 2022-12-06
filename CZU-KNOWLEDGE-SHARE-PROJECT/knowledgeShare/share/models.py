from django.db import models
from django.contrib.auth.models import AbstractUser


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "faculty"
        verbose_name_plural = "faculties"

    def __str__(self):
        return self.name


class StudyType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "studytype"
        verbose_name_plural = "studytypes"

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    study_type = models.ForeignKey(StudyType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return self.last_name + " " + self.first_name


class StaffCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "staffcategory"
        verbose_name_plural = "staffcategories"

    def __str__(self):
        return self.name


class Administrator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    staff = models.ForeignKey(StaffCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "administrator"
        verbose_name_plural = "administrators"

    def __str__(self):
        return self.last_name + " " + self.first_name


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    administrator = models.ForeignKey(
        Administrator, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        if self.student is not None:
            return f"{self.student.last_name} {self.student.first_name}"
        elif self.administrator is not None:
            return f"{self.administrator.last_name} {self.administrator.first_name}"
        return self.username


class Subject(models.Model):

    CHOICES = ((1, "Activate"), (2, "Deactivate"))

    subject_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "subject"
        verbose_name_plural = "subjecs"

    def __str__(self):
        return f"{self.subject_code} : {self.name}"


class File(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to="images/cover", null=True)
    file_link = models.FileField(upload_to="documents/")
    is_public = models.BooleanField(default=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "file"
        verbose_name_plural = "files"

    def __str__(self):
        return self.title


class FilePermission(models.Model):

    CHOICES = ((1, "Approved"), (2, "Denied"), (3, "Pending"))

    requester = models.ForeignKey(
        User, related_name="requester", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    file_link = models.ForeignKey(File, on_delete=models.CASCADE)
    status = models.IntegerField(choices=CHOICES, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "file_permission"
        verbose_name_plural = "files_permission"

    def __str__(self):
        return self.file_link.title


class FileView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_link = models.ForeignKey(File, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "file_view"
        verbose_name_plural = "file_views"

    def __str__(self):
        return self.user


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_link = models.ForeignKey(File, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.comment

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.title