
Welcome to the **Django Authentication System**! This project implements a robust and user-friendly authentication system for login and signup functionality using Django.

---

## 🚀 Features

- **Secure User Authentication**: Leveraging Django's built-in authentication system.
- **Signup Functionality**: Users can create accounts with form validation.
- **Login System**: Registered users can log in to their accounts securely.
- **Password Hashing**: User passwords are stored securely using hashing.
- **Session Management**: Ensures secure user sessions.

---

## 📂 Project Structure

\`\`\`
authentification/
├── manage.py
├── db.sqlite3
├── authentication/ 
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
\`\`\`

---

## 🛠️ Installation and Setup

### Prerequisites

Ensure you have the following installed:
- Python (3.8 or higher)
- pip
- Virtualenv (recommended)

### Steps

1. **Clone the Repository**

   \`\`\`bash
   git clone https://github.com/Rochdi7/Django-Projects/authentification.git
   cd django-auth-system
   \`\`\`

2. **Create a Virtual Environment**

   \`\`\`bash
   python -m venv env
   source env/bin/activate  # On Windows, use \`env\\Scripts\\activate\`
   \`\`\`

3. **Install Dependencies**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Apply Migrations**

   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Run the Server**

   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. **Access the Application**

   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🖥️ Screenshots

### Login Page
![Login Page](screenshots/login.png)

### Signup Page
![Signup Page](screenshots/signup.png)

---

## 🤝 Contribution

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes and push them.
4. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the \`LICENSE\` file for more details.

---

## 🌟 Acknowledgements

- Thanks to the Django team for their amazing framework.

---

Made with ❤️ using Django!" > README.md
