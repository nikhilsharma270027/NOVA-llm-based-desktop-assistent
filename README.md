"# 🚀 Nova - Your Intelligent Desktop Companion

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange)]()

**Nova** is a powerful, privacy-first AI desktop assistant that runs 100% locally on your machine. Control your computer with natural language commands, access your files intelligently, and automate repetitive tasks—all without sending your data to the cloud.

## ✨ Key Features

### 🎙️ Voice Control
- **Wake word detection** - Say "Hey Nova" to activate
- **Offline speech recognition** using Vosk
- **Natural language understanding** powered by local Ollama (Qwen 2.5 LLM)
- **Text-to-speech feedback** for all interactions

### 🤖 Smart Automation
- **Application Control** - Open apps, launch websites, manage windows
- **File Management** - Find files by name, type, date, or keywords
- **System Control** - Sleep, shutdown, brightness, volume management
- **Media Control** - Play/pause music, skip tracks, adjust volume
- **Screenshot & Recording** - Capture screens and record audio
- **Clipboard History** - Access and manage clipboard entries
- **Activity Tracking** - Monitor running applications and window focus

### 📱 Multiple Interfaces
- **Voice Command** - Hands-free control with wake word detection
- **Telegram Bot Integration** - Control your computer remotely via Telegram
- **Browser Extension** - Seamless integration with Firefox and Chrome
- **Desktop UI** - Real-time status and feedback

### 📊 Intelligent Features
- **Memory System** - Learns your preferences and habits
- **Activity Logging** - Tracks your work patterns
- **Research Agent** - Performs web searches in background
- **Safety Overrides** - Prevents LLM hallucinations for critical commands

### 🔒 Privacy & Security
- **100% Local Processing** - No cloud dependencies
- **100% Private** - Your data never leaves your computer
- **Open Source** - Full transparency and community auditing
- **Optional Telegram** - Self-hosted communication

## 🏗️ System Architecture

```
INPUT (Senses)
   ↓
├─ 🎤 Voice Listener (Wake word + STT)
├─ 💬 Telegram Bot
└─ 🌐 Browser Extension

PROCESSING (Brain)
   ↓
├─ 🧠 Memory Context (preferences, history)
├─ 🤖 Ollama LLM (Intent Classification)
└─ ⚡ Safety Validation

EXECUTION (Muscles)
   ↓
├─ 🖥️ System Commands
├─ 🌐 Browser Control
├─ 📁 File Operations
├─ 🎵 Media Control
└─ 📸 Screen Capture
```

## 📋 Supported Commands

| Command Type | Examples |
|---|---|
| **App Control** | "Open Chrome", "Launch Spotify", "Close Notepad" |
| **File Management** | "Find my resume", "Show recent documents", "Where's my project file" |
| **System** | "Sleep", "Shutdown", "Increase brightness", "Mute" |
| **Media** | "Play music", "Next song", "Pause", "Volume to 50%" |
| **Info** | "Battery status", "Show running apps", "What time is it" |
| **Capture** | "Take screenshot", "Record audio for 10 seconds" |
| **Web** | "Search for Python tutorials", "Open GitHub" |

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **Ollama** ([Download](https://ollama.com)) - Local AI engine
- **Git** (optional) - For easy cloning
- **Windows 10+** or **Linux**

### Installation (Windows)

#### Automated Setup (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/nova2.git
cd nova2

# 2. Run the setup script
./setup.bat

# 3. Start Nova
./start_nova.bat
```

#### Manual Setup
```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download Ollama model
ollama pull qwen2.5

# 4. Start the application
python -m nova.main
```

### Installation (Linux)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/nova2.git
cd nova2

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download Ollama model
ollama pull qwen2.5

# 5. Start Nova
python -m nova_linux.main
```

## 📚 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[User Manual](docs/USER_MANUAL.md)** - How to use Nova
- **[System Architecture](docs/ARCHITECTURE.md)** - Technical design and flow
- **[Configuration Guide](docs/CONFIGURATION.md)** - Customize settings
- **[Browser Extension Guide](docs/EXTENSION_INSTALL_GUIDE.md)** - Install browser extensions
- **[Activities Feature Guide](docs/ACTIVITIES_FEATURE_GUIDE.md)** - Monitor app usage
- **[Location Accuracy Guide](docs/LOCATION_ACCURACY_GUIDE.md)** - File search tips

## 🔧 Configuration

Edit `src/nova/utils/settings.py` to customize:

```python
# Voice settings
WAKE_WORDS = ["hey nova", "hey you"]
STT_ENGINE = "vosk"  # or "google"

# LLM settings
LLM_MODEL = "qwen2.5"
OLLAMA_HOST = "http://localhost:11434"

# Features
ENABLE_TELEGRAM = True
ENABLE_FILE_TRACKING = True
ENABLE_ACTIVITY_LOGGING = True

# Telegram bot token (if enabled)
TELEGRAM_BOT_TOKEN = "your_token_here"
TELEGRAM_CHAT_ID = "your_chat_id_here"
```

## 🎯 Usage Examples

### Voice Commands
```
You: "Hey Nova"
Nova: [beep] "Listening..."

You: "Open Chrome and search for Python tutorials"
Nova: [opens Chrome, searches for Python tutorials] "Done!"

You: "Find my resume from last month"
Nova: [searches files] "Found: Resume_2025.pdf on Desktop"

You: "What time is it and what apps are running?"
Nova: "It's 2:30 PM. You have Chrome, VS Code, and Spotify running."
```

### Telegram Bot
Send commands via Telegram:
```
/start - Show help
"Open Spotify" - Voice command via text
"Show battery" - Check system info
"Take screenshot" - Capture screen
```

### Browser Extension
Click the Nova extension icon to:
- Execute commands in your browser context
- Search selected text
- Quick access to clipboard history

## 📦 Project Structure

```
nova2/
├── src/
│   ├── nova/              # Windows version
│   │   ├── main.py        # Entry point
│   │   ├── agents/        # Command executors
│   │   ├── core/          # Brain, voice, memory
│   │   └── features/      # Clipboard, files, activity
│   └── nova_linux/        # Linux version
├── browser_extension/     # Chrome/Edge extension
├── firefox_extension/     # Firefox extension
├── docs/                  # Documentation
├── model/                 # Speech recognition models
└── setup.bat              # Installation script
```

## 🔌 API & Integration

### Local API Endpoints
- **Ollama**: `http://localhost:11434/api/generate`
- **Telegram Bot**: Configured via environment variables
- **Browser Extension**: Native messaging via native manifest

### Extensibility
Nova is designed to be extended:
- Add custom commands in `agents/system.py`
- Create new features in `features/`
- Build custom integrations with the Brain module

## 🐛 Troubleshooting

### Nova doesn't respond to wake word
- Check microphone is connected and working
- Verify Vosk model is downloaded
- Check audio levels: Run `python list_audio_devices.py`
- Test STT: Say a command after hearing the beep

### Commands not executing
- Check Ollama is running: `ollama serve`
- Verify model is installed: `ollama list`
- Check Brain logs for intent classification errors

### File search not finding files
- Enable file tracking: Set `ENABLE_FILE_TRACKING = True`
- Wait for initial indexing (first run takes time)
- Check file permissions and path settings

For more help, see [USER_MANUAL.md](docs/USER_MANUAL.md)

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** and test thoroughly
4. **Commit with clear messages** (`git commit -m 'Add amazing feature'`)
5. **Push to your branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ollama** - Local LLM runtime
- **Vosk** - Offline speech recognition
- **SpeechRecognition** - Audio processing
- **PyAutoGUI** - Desktop automation
- **Python Telegram Bot** - Telegram integration

## 📞 Support & Community

- **Issues**: Report bugs on [GitHub Issues](https://github.com/YOUR_USERNAME/nova2/issues)
- **Discussions**: Join community discussions on GitHub
- **Documentation**: Check [docs/](docs/) folder for detailed guides

## 🚦 Roadmap

- [ ] GPU acceleration for LLM inference
- [ ] Multi-language support
- [ ] Web-based dashboard
- [ ] Mobile app integration
- [ ] Custom wake word training
- [ ] Plugin marketplace
- [ ] Advanced scheduling

## 📊 Project Stats

- **Lines of Code**: 5000+
- **Python Modules**: 15+
- **Supported Platforms**: Windows, Linux
- **Languages**: Python, JavaScript (extensions)
- **Local Processing**: 100%
- **Cloud Dependency**: 0%

---

**Made with ❤️ by the Nova community**

⭐ If you find this project useful, please consider giving it a star!

**[⬆ Back to Top](#-nova---your-intelligent-desktop-companion)**" 
