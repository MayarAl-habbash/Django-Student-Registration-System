# 🎓 StudentHub — Django Student Registration System

A modern, responsive **Student Registration and Management System** built with Django.

StudentHub provides a clean interface for registering students, validating their information, uploading profile images, and displaying registered student records in an organized directory.

The project demonstrates the integration of **Django Models, ModelForms, Custom Validation, Views, Templates, and Database Operations**.

---

## ✨ Project Features

- **Student Registration:** Register students using seven required fields.
- **Custom Form Validation:** Validate student information before saving it.
- **Unique University IDs:** Prevent duplicate university ID numbers.
- **Image Uploads:** Upload JPG and PNG student images.
- **Student Directory:** Display registered students in a formatted table.
- **Django Admin:** Manage student records through the administration panel.
- **Responsive Design:** Modern interface with a soft purple color palette.
- **Error Handling:** Display clear validation messages for incorrect inputs.

---

## 📸 Project Screenshots

### 1. Student Registration Form

A modern registration form featuring seven required fields, custom validation, and image upload functionality.

![Student Registration Form](SCREENSHOTS/Student_Registration_Form.png)

### 2. Student Directory

A responsive student directory displaying registered students, their information, and profile images.

![Registered Students Table](SCREENSHOTS/Registered_Students_Table.png)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| Django ModelForm | Form generation and validation |
| SQLite | Database management |
| HTML5 | Page structure |
| CSS3 | Interface design and responsiveness |
| Pillow | Image validation and processing |
| Git & GitHub | Version control and project hosting |

---

## 📋 Student Registration Fields

The registration form contains seven required fields with the following validation rules:

| Field | Validation |
|---|---|
| Full Name | Letters and spaces only |
| University ID | Exactly 9 digits, starts with 1 or 2, and must be unique |
| National ID | Exactly 9 digits, starts with 9, 8, or 4 |
| Mobile Number | Exactly 10 digits, starts with 059 or 056 |
| Address | Maximum 150 characters |
| Date of Birth | Must be a valid date |
| Student Image | JPG or PNG only |

Validation is implemented using Django's built-in field validation and custom `clean_<field>()` methods.

---

## 📁 Project Structure

```text
Student-Registration-Assignment/
│
├── StudentRegistration/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── static/
│   │   └── students/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── templates/
│   │   └── students/
│   │       ├── register.html
│   │       └── student_list.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── SCREENSHOTS/
│   ├── Student_Registration_Form.png
│   └── Registered_Students_Table.png
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The virtual environment, SQLite database, and uploaded media files are excluded from version control.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MayarAl-habbash/Django-Student-Registration-System.git
```

Navigate to the project directory:

```bash
cd Django-Student-Registration-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows CMD:**

```cmd
venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Django Secret Key

For security, the Django secret key is loaded from the `DJANGO_SECRET_KEY` environment variable.

Generate a secret key using Django:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set the generated key as an environment variable.

**Windows CMD:**

```cmd
set "DJANGO_SECRET_KEY=your-generated-secret-key"
```

**Windows PowerShell:**

```powershell
$env:DJANGO_SECRET_KEY = "your-generated-secret-key"
```

Replace `your-generated-secret-key` with the actual generated value.

Keep this key private and do not commit it to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

Django will create the required SQLite database tables.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔗 Application Pages

| Page | Local URL |
|---|---|
| Student Registration | `http://127.0.0.1:8000/` |
| Student Directory | `http://127.0.0.1:8000/students/` |
| Django Administration | `http://127.0.0.1:8000/admin/` |

---

## 🔐 Django Administration

The application supports Django's built-in administration panel.

To create an administrator account, run:

```bash
python manage.py createsuperuser
```

Follow the instructions to create your account.

Then start the development server and visit:

```text
http://127.0.0.1:8000/admin/
```

The Student model is registered in Django Admin, allowing authorized administrators to manage student records.

---

## ✅ Validation & Testing

The application includes validation for:

- Alphabetic student names.
- University ID length, prefix, and uniqueness.
- National ID length and prefix.
- Mobile number format.
- Address length restrictions.
- Valid dates.
- Accepted image formats.

Invalid form submissions display field-specific error messages without saving the student record.

Successful submissions save the student's information and redirect the user to the Student Directory.

---

## 📝 Additional Notes

- The project uses **SQLite** as its local database.
- Uploaded student images are stored in the configured `media/student_images/` directory.
- Uploaded media files and local database records are not included in the GitHub repository.
- The screenshots demonstrate the application using sample student data.
- The project is intended for educational use and local development.

---

## 👩‍💻 Project Information

**Project:** StudentHub — Django Student Registration System  
**Developer:** Mayar Alhabbash  
**Framework:** Django  
**Language:** Python  
**Purpose:** Web Programming — Django Forms Assignment

---

<p align="center">
  <strong>StudentHub</strong><br>
  A clean and modern approach to student registration.
</p>