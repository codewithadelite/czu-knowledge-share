![Logo](https://raw.githubusercontent.com/codewithadelite/czu-knowledge-share/knowledge-share-app/CZU-KNOWLEDGE-SHARE-PROJECT/knowledgeShare/static/images/czu-k-s-logo.png)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# Introduction

CZU knowledge share is platform that will allow all CZU students to help each
other by sharing their self-study papers, drafts instead of throwing them away after
study, so that other students can use those papers for their self-study and research
as well.
And this web application provide REST API endpoints to allow communication with C#
(Window Form) application for some functionality that will be described below.

## 📷 Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Features

1. **Administration:**

- Admin is able to view total students registered, total files
  students have shared….. and other information.
- Admin is able to CRUD (Create, Read, Update, Delete) faculties,subjects.

2. **Students:**

- Student is able to upload his/her PDF file that contains all images for his/her self-study papers, drafts and the link to the PDF file is stored in Database.
- Once student uploads file is able to set permissions over his file where he can set it to be public or private (means when some students need the file, they will have to request for it, and student who is owner of the file will be able to grant permission or refuse actually to student who have requested for it).
- When student has permission to view shared file or file is set to public by its owner, student will be able to comment (share his idea) and view other student’s comments.
- When student opens the shared file page, the system will record in database that student has viewed the file, and the system will avoid to record this more than once in case the same student is viewing the shared file again.
- When student is sharing file that contains self-study papers, is able to select the subject that file belongs to.

3. **C# (Window Form):**

- This application allows to assign task to one of administrators of this web application using REST API communication in JSON format (The logic behind this, is that C# app sends **title** and **description** of the task to the endpoint with POST HTTP request, and on the server side with PYTHON , all admins registered in DB are selected and the system choose one to assign task randomly and send back response to C# application with the name of the admin the task is assigned to) .
- This application allows to display all tasks that are in DB using GET HTTP request and shows the status of these task (It means **DONE** or **PENDING**).

## Run Locally

Clone the project

```bash
  git clone https://github.com/codewithadelite/czu-knowledge-share/tree/knowledge-share-app
```

Go to the project directory

```bash
  cd knowledgeShare
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  py manage.py runserver
```

## Tech Stack

**Client:** HTML, CSS, JAVASCRIPT, BOOTSTRAP

**Server:** Python, Django, Django REST Framework.

**Database:** SQLite wrapped into Django ORM.

**Tools:** Git, Github.
