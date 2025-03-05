# TODO Application

This is a simple **TODO** application built using **Django**. It allows users to add, view, update, and delete tasks. The project includes user authentication features like **Login** and **Signup** and uses **MySQL** as the database.

## Features

- **User Authentication**:
  - **Signup**: Users can register with a username and password.
  - **Login**: Users can securely log in.

- **TODO Operations**:
  - **Create**: Users can add new tasks.
  - **Read**: Users can view their tasks.
  - **Update**: Users can edit their tasks.
  - **Delete**: Users can delete tasks.

- **Database**: Uses **MySQL** to store user and task data.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Django** (Install via `pip`)
- **MySQL** (Ensure MySQL is installed)
- **MySQL client library for Python** (`mysqlclient`)

---

### Steps to Set Up

```bash
1. Clone the repository:
   git clone https://github.com/sahilthagyal/MY-TODOs.git

2. Navigate to the project directory:
   cd todo

3. Create and activate a virtual environment:
   - On **Windows**:
     python -m venv venv
     venv\Scripts\activate
   - On **Mac/Linux**:
     python3 -m venv venv
     source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Install MySQL client for Python:
   pip install mysqlclient

6. Configure MySQL database settings in `settings.py`:
   - Open `settings.py` and modify the `DATABASES` setting:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
7. Create the MySQL database:
   ```sql
   CREATE DATABASE your_db_name;
   ```

8. Run migrations:
   python manage.py migrate

9. Create a superuser:
   python manage.py createsuperuser

10. Run the development server:
    python manage.py runserver

11. Visit the app in your browser:
    http://127.0.0.1:8000/

Now, you can log in and manage your tasks efficiently!
