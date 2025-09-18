# 🐍 Python Installation & Virtual Environment Setup Guide

This guide helps you install Python and set up a virtual environment (venv) on **Windows** and **macOS**. A virtual environment keeps your project dependencies isolated and organized.

---

## 📦 Step 1: Install Python

### 🔹 Windows

1. Go to the official Python website: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Download the latest **Python 3.x** installer for Windows.
3. Run the installer:
   - ✅ Check **"Add Python to PATH"** before clicking "Install Now".
   - Wait for installation to complete.
4. Verify installation:
   ``` python --version```

### 🔹 macOS

1. Open Terminal.

2. Check if Python 3 is already installed:

```python3 --version```

### If not installed, use Homebrew (recommended):

### Install Homebrew (if not already installed):
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)```

## Install python 
```brew install python```

## Verify 
```python3 --version```

### 🧪 Step 2: Create a Virtual Environment [OPTIONAL]

#### 🔹 Windows

1. Open Command Prompt or PowerShell.

2. Navigate to your project folder:

`cd path\to\your\project`

3. Create a virtual environment:
   
`python -m venv venv`

4. Activate the environment:

`.\venv\Scripts\activate`

5. To deactivate:

 `deactivate`

#### 🔹 macOS

1. Open Terminal.

2. Navigate to your project folder:
```cd /path/to/your/project```

3. Create a virtual environment:

``` python3 -m venv venv ```

4. Activate the environment:

``` source venv/bin/activate```

5. To deactivate:

``` deactivate```




