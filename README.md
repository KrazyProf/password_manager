# 🔐 Password Manager
A simple yet powerful Password Manager built with Python and Tkinter. It allows you to generate secure passwords, save and retrieve login credentials for websites, and store them safely in a local JSON file.


### 🧩 Features
✅ Secure password generator with letters, numbers, and symbols

💾 Save credentials (website, email, password) to a local JSON file

🔍 Search and retrieve saved credentials by website name

📋 Automatic copy of the generated password to clipboard

🖼️ Clean and interactive GUI built using Tkinter

### 🛠️ Installation
Clone or download the repository
Make sure you have main.py and logo.png in the same directory.

Install required packages
Tkinter comes with Python, but for clipboard functionality, install pyperclip:

```bash
pip install pyperclip
```
Run the app

```bash
python main.py
```

### 📂 File Structure
```bash
.
├── main.py        # Main application script
├── logo.png       # Logo image for UI
└── password.json  # Auto-created on first save; stores your passwords
```

### 🧠 How It Works
Enter the website and email.

Generate a strong password or type your own.

Click Add to save the credentials.

Use Search to retrieve existing credentials.

Passwords are stored securely in password.json.

### 🔐 Security Note
This app stores passwords locally in a .json file. Make sure the file is stored securely.

You may add encryption or link with a cloud storage option for enhanced safety (future enhancement idea).

### 💡 Dependencies
Python 3.x

Tkinter (comes with Python)

pyperclip for clipboard functionality

### 📷 Preview
- **![download (1)](https://github.com/user-attachments/assets/ed1d3764-ed9c-4581-a2c2-7d0f2bf521e0)**

### ✍️ Author
Ayush Kaithwas
