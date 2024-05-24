# Office Employee Management System

This project is a Django-based web application designed to manage office employees. It provides functionalities to add, update, and delete employee records, as well as view detailed information about employees.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

The Office Employee Management System is designed to streamline the process of managing employee information within an organization. This system allows administrators to perform CRUD (Create, Read, Update, Delete) operations on employee records.

## Features

- **Add Employee:** Add new employee records to the system.
- **Update Employee:** Edit existing employee information.
- **Delete Employee:** Remove employee records from the system.
- **View Employee:** View detailed information about each employee.

## Installation

To get started with the Office Employee Management System, follow these steps:

1. **Clone the repository:**

```bash
git clone https://github.com/sunil98600/Office-Employee-Management-System.git
cd office-employee-management-system
```

2. **Create a virtual environment:**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

5. **Run the development server:**

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

1. **Navigate to the homepage:** Open the `index.html` file in your web browser.
2. **Add a new employee:** Use the form provided to add a new employee record.
3. **Update an employee:** Click on an employee record to edit the details.
4. **Delete an employee:** Click on the delete button next to an employee record to remove it.
5. **View an employee:** Click on an employee's name to view detailed information.

## Project Structure

```
office-employee-management-system/
├── office_emp_proj/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── emp_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│       ├── __init__.py
│       └── __pycache__/
│   └── templates/
│       └── index.html
├── manage.py
├── requirements.txt
└── README.md
```

- `office_emp_proj/`: The Django project directory.
- `emp_app/`: The main app containing models, views, URLs, and templates.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static files (if any).
- `manage.py`: Django command-line utility.
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
