# Django URL Shortener

A simple and interactive URL shortener built with **Python Django**.  
It allows users to shorten long URLs, track expiry dates for links, and redirect shortened URLs to their original destinations.  
Includes a Bootstrap-based responsive UI and an optional Docker setup for easy deployment.

---

## 🚀 Features
- Shorten any valid URL
- Redirect from short link to original URL
- Set expiry dates for links
- Store data in SQLite database
- Responsive UI using **Bootstrap**
- Dockerized for quick deployment
- Clean and maintainable Django codebase

---

## 📂 Project Structure
```
.
├── shortener/                  # Django app
│   ├── migrations/
│   ├── templates/shortener/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── result.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── url_shortener/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── README.md
```

---

## ⚙️ Installation (Without Docker)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AswinPC333/IOSS.git
cd IOSS
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Start the Server
```bash
python manage.py runserver
```

The app will be available at: **http://127.0.0.1:8000**

---

## 🐳 Running with Docker

### 1️⃣ Build & Run
```bash
docker-compose up --build
```

### 2️⃣ Access App
Go to: **http://127.0.0.1:8000**

---

## 🔧 Environment Variables
You can set environment variables in `.env` (optional):
```
DEBUG=1
```

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact
Created by [Aswin p c](https://github.com/AswinPC333) - feel free to reach out!
