## ⚙️ Linux Installation Guide

This guide covers everything you need to get the **Nova Linux Telegram Bot** running on your Linux machine.

> _note: Linux port for nova is still in a very early stage_

---

### Prerequisites

| Requirement      | Version | Download                                        |
| ---------------- | ------- | ----------------------------------------------- |
| **Python**       | 3.10+   | [python.org](https://www.python.org/downloads/) |
| **Ollama**       | Latest  | [ollama.com](https://ollama.com/)               |
| **Telegram Bot** | Token   | [@BotFather](https://t.me/BotFather)            |

### Step 1:

Clone the repository.

```bash
git clone https://github.com/Surajkumar5050/nova-assistant.git
cd nova-assistant
```

### Step 2:

Set up your environment Variables:

1. make your .env file.

```bash
cp .env.example .env
```

2. Set up your .env

```env
TELEGRAM_TOKEN=your_bot_token_here
ALLOWED_TELEGRAM_USERNAME=your_telegram_username
MODEL_NAME=qwen2.5-coder:7b # Set to whichever model best works for you.
OFFLINE_MODE=false # Set to true for 100% offline privacy
LOG_LEVEL=INFO
```

### Step 3:

go to `./pyproject.toml`.

1. Comment out the `pywin32` dependency.

```toml
dependencies = [
    "SpeechRecognition",
    "pyttsx3",
    "pyaudio",
    "pillow",
    "textblob",
    "requests",
    "python-telegram-bot",
    "psutil",
    # "pywin32", <- Should look like this
    "pyautogui",
    "opencv-python",
    "wmi",]
```

2. [Optional] Comment out the `nova:main` entry point.

```toml
[project.scripts]
# nova = "nova.main:main"
nova-linux = "zyron_linux.main:main"
```

### Step 4:

Set up your venv.

```bash
python -m venv .venv
```

### Step 5:

pip install the current directory.

```bash
pip install .
```

for **development** use the `-e` flag.

```bash
pip install -e .
```

This should install all the dependencies required for the project to run.

### Step 6:

For now to run the telegram Agent simply run the `zyron_linux.agents.telegram` module.

```bash
python -m zyron_linux.agents.telegram
```

#### Note: Linux port for nova is still in development stage, feel free to contribute or report any issues
