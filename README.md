# Task Manager (Flask Web App)
A simple Flask-based Task Manager that allows users to add, complete, and delete tasks. Built with Flask, PostgreSQL, and Bootstrap.

## Features
- User authentication (register, login, logout)
- Task management (add, mark as complete, delete)
- Flask-SQLAlchemy for database management
- Flask-WTF for form validation
- Bootstrap for a responsive UI

## Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy, Flask-WTF
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 5
- **Authentication:** Flask-Login, Werkzeug

## Installation Guide
Follow these steps to set up the project on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/adamdagenais/task-manager.git
cd task-manager
```

### 2. (Optional) Create a Virtual Environment
It is recommended to use a virtual environment to isolate dependencies.

#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

To deactivate the virtual environment:
```bash
deactivate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://your_username:your_password@localhost/task_manager
```

### 5. Set Up the Database
```bash
flask db upgrade
```
If migrations are missing, initialize them:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application
```bash
python run.py
```
The application will be running at:  
**http://127.0.0.1:5000/**

---

## Usage Instructions
- Register/Login
- Add Tasks
- Mark Tasks as Completed
- Delete Tasks
- Logout

---

## Troubleshooting
### 1. **Flask Not Found or Import Errors**
Make sure the virtual environment is activated:
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```
Then reinstall dependencies:
```bash
pip install -r requirements.txt
```

### 2. **Database Migration Issues**
If you get database migration errors, try:
```bash
flask db stamp head
flask db migrate -m "Fix migration"
flask db upgrade
```

### 3. **Environment Variables Not Loading**
Ensure `.env` exists and is correctly formatted. If issues persist, manually export them:
```bash
export SECRET_KEY=your_secret_key_here
export DATABASE_URL=postgresql://your_username:your_password@localhost/task_manager
```

---

## Future Improvements
- API integration for mobile apps
- Task categories & due dates
- Dark mode UI

---

## Contributing (Optional)
If you'd like to contribute:
1. Fork this repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/task-manager.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Added feature-name"
   ```
5. Push and create a pull request:
   ```bash
   git push origin feature-name
   ```

---

## License (Optional)
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact
If you have any questions, feel free to contact me via GitHub or email.
