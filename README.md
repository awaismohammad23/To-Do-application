# Django To-Do Application

A fully functional To-Do management system built with Django and Bootstrap 5.

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as completed/pending
- ✅ Beautiful, responsive UI with Bootstrap 5
- ✅ Task descriptions (optional)
- ✅ Automatic timestamps
- ✅ Django admin interface
- ✅ Unit tests included

## Requirements

- Python 3.8 or higher
- Django 4.2 or higher

## Installation & Setup

### 1. Navigate to the project directory

```bash
cd "To-do app django"
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Run migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
todo_project/
├── manage.py
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── tests.py
│   └── templates/
│       └── tasks/
│           ├── base.html
│           ├── task_list.html
│           ├── task_detail.html
│           ├── task_form.html
│           └── task_confirm_delete.html
└── README.md
```

## URL Routes

- `/` - Task list view (homepage)
- `/task/<id>/` - Task detail view
- `/task/create/` - Create new task
- `/task/<id>/edit/` - Update task
- `/task/<id>/delete/` - Delete task
- `/task/<id>/toggle/` - Toggle task completion status
- `/admin/` - Django admin interface

## Running Tests

To run the unit tests:

```bash
python manage.py test tasks
```

## Usage

1. **View all tasks**: Navigate to the homepage to see all your tasks
2. **Create a task**: Click "Add New Task" or "New Task" in the navigation
3. **View task details**: Click "View" on any task card
4. **Edit a task**: Click "Edit" on any task
5. **Mark as complete**: Click "Complete" button or use the toggle function
6. **Delete a task**: Click "Delete" and confirm the deletion

## Database

The application uses SQLite by default. The database file (`db.sqlite3`) will be created automatically after running migrations.

## Admin Interface

Access the Django admin at `/admin/` using the superuser credentials created in step 5. You can manage tasks directly from the admin panel.

## Technologies Used

- **Django 4.2+** - Web framework
- **Bootstrap 5** - Frontend CSS framework
- **SQLite** - Database
- **Bootstrap Icons** - Icon library

## License

This project is open source and available for educational purposes.
