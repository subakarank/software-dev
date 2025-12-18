# 🐍 Python Installation & Virtual Environment Setup on Windows

This guide explains **how to install Python on Windows**, **verify the installation**, and **create a virtual environment** to start learning Python.

---

## 🔹 Step 1: Download Python for Windows

1. Open your browser
2. Go to the official Python website:
   
   https://www.python.org/downloads/

3. Click **Download Python 3.x.x** (latest version)

---

## 🔹 Step 2: Install Python (IMPORTANT)

1. Double-click the downloaded installer (`python-3.x.x.exe`)
2. **IMPORTANT:** Enable the checkbox below:
   
   - ✅ **Add Python to PATH**
3. Click **Install Now**
4. Wait until you see **"Setup was successful"**

---

## 🔹 Step 3: Verify Python Installation

1. Press **Windows + R**
2. Type `cmd` and press **Enter**
3. Run the following command:

```bash
python --version
```

or

```bash
python -V
```

✅ Expected output:

```text
Python 3.x.x
```

---

## 🔹 Step 4: Verify pip Installation

`pip` is Python’s package manager.

Run:

```bash
pip --version
```

✅ Expected output:

```text
pip 23.x.x from ...
```
If you get error when you check in pip version 
```
'pip' is not recognized as an internal or external command,
operable program or batch file.
```
Then add these into PATH environment variables
```
C:\Users\[username]\AppData\Local\Python\PythonCore-3.14-64\
C:\Users\[username]\AppData\Local\Python\PythonCore-3.14-64\Scripts\
```
# How to add into PATH

- Press Windows + R
- Type sysdm.cpl → Enter
- Advanced tab → Environment Variables
- Under User variables → select Path → Edit
- Click New → paste both paths (one by one)
- Click OK → OK


---

## 🔹 Step 5: Create a Project Folder

1. Open **File Explorer**
2. Go to **Documents** (or any preferred location)
3. Create a new folder named:

```text
python-learning
```

---

## 🔹 Step 6: Open Command Prompt Inside Project Folder

1. Open the `python-learning` folder
2. Click the **address bar**
3. Type `cmd` and press **Enter**

This opens Command Prompt in the project directory.

---

## 🔹 Step 7: Create a Virtual Environment

Run the following command:

```bash
python -m venv venv
```

📁 A folder named `venv` will be created.

---

## 🔹 Step 8: Activate Virtual Environment (Windows)

Run:

```bash
venv\Scripts\activate
```

✅ You should see:

```text
(venv)
```

at the beginning of the command line.

---

## 🔹 Step 9: Upgrade pip (Recommended)

```bash
python -m pip install --upgrade pip
```

---

## 🔹 Step 10: Install Python Packages (Example)

```bash
pip install requests
```

Verify installation:

```bash
pip list
```

---

## 🔹 Step 11: Create and Run First Python Program

1. Create a file named `hello.py`
2. Add the following code:

```python
print("Hello, Python!")
```

3. Run the program:

```bash
python hello.py
```

✅ Output:

```text
Hello, Python!
```

---

## 🔹 Step 12: Deactivate Virtual Environment

When finished, run:

```bash
deactivate
```

---

## 📁 Recommended Project Structure

```text
python-learning/
│
├── venv/
├── hello.py
└── requirements.txt
```

---

✅ You are now ready to start learning Python using a virtual environment.

