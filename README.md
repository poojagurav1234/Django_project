# ATM Management System

This is a Django-based web application for managing ATM sites. The system allows users to upload Excel files containing ATM site details and stores them in a database. It also provides a view to list all the uploaded ATM sites.

## Features

- **Upload ATM Site Data**: Users can upload an Excel file containing ATM site details.
- **Store Data**: The uploaded data is stored in a PostgreSQL database.
- **List ATM Sites**: A view to list all the uploaded ATM sites.

## Installation

### Prerequisites

- Python 3.x
- Django 4.2.x
- pandas
- psycopg2-binary
- PostgreSQL

### Steps to Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/poojagurav1234/oneture-tech_project/tree/master/atm_management_system.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd atm_management_system
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (to access the Django admin panel):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the Admin Panel**:
    - Go to `http://127.0.0.1:8000/admin/`
    - Login with the superuser credentials created earlier.

2. **Upload ATM Site Data**:
    - Navigate to `http://127.0.0.1:8000/upload/`
    - Choose an Excel file and upload.

3. **View Uploaded ATM Sites**:
    - Navigate to `http://127.0.0.1:8000/sites/`
