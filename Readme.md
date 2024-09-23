# RweetBlog

A Django-based web application for creating and sharing "Rweets." 
This README will guide you through the steps to set up, run, and contribute to the project.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Database Setup](#database-setup)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication (login, registration, and password reset).
- Create, edit, delete tweets.
- Upload images along with tweets.
- Responsive design using Bootstrap.
- Password reset via email.

## Requirements

Before starting, ensure you have the following installed:

- Python 3.9 or greater version
- Django 5.1.1 or other newest.
- PostgreSQL (or SQLite if you're using the default database)
- Git
- Pip (Python package manager)
- A virtual environment tool like `venv` or `virtualenv`

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tweetblog.git
cd tweetblog
```

### 2. Setup Virtual Environment

- for Windows:
```bash
python -m venv .venv
.venv/Scripts/activate
```
-for Linux/macOS :
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
### 1. Create a .env file in the root directory (if not present):
```bash
touch .env
```
Or you can create manually

### 2. Add environment variable to the ```.env``` file
```bash
# for database configuration
#DataBase --PostgreSQL
DB_NAME=your_database_name
DB_USER=your_database_user #postgres
DB_PASSWORD=your_database_password
DB_HOST=host_name #localhost
DB_PORT=port_name  #5432

# for email configuration using smtp
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

```
Make sure to replace the placeholders with actual values for your project.

### 3. Set up the .gitignore file to exlude .env and other sensitive files:
```bash
echo '.env' >> .gitignore
```
Or you can create manually .gitignore file in you root directory if not exist and add the .env into the file

## Running the Project
### 1. Migrate the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create a Superuser
```bash
python manage.py createsuperuser

```
Follow up the prompts to create a superuser account.

### Run the Development Server
```bash
python manage.py runserver

```
Visit the application https://127.0.0.1:8000 .

---
## Database Setup (for PostgreSQL)
### 1. Install PostgreSQL and create a database:


```bash
CREATE USER your_user WITH PASSWORD 'your_password';
ALTER ROLE your_user SET client_encoding TO 'utf8';
ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tweetblog TO your_user;
\q
```
---
## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.





