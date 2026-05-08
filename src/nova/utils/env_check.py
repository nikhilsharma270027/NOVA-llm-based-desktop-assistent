import importlib
import sys

def check_dependencies():
    """
    Checks if all required core dependencies are installed.
    If anything is missing, it provides a friendly message instead of a crash.
    """
    required = [
        ("ollama", "ollama"),
        ("telegram", "python-telegram-bot"),
        ("psutil", "psutil"),
        ("pydantic_settings", "pydantic-settings"),
        ("idna", "idna"),
        ("numpy", "numpy"),
        ("pyperclip", "pyperclip")
    ]
    
    missing = []
    
    for module_name, package_name in required:
        try:
            importlib.import_module(module_name)
        except ImportError:
            missing.append(package_name)
            
    if missing:
        print("\n" + "!" * 60)
        print(" 🚨 MISSING DEPENDENCIES DETECTED 🚨")
        print("!" * 60)
        print("\nNova needs the following libraries to run:")
        for lib in missing:
            print(f"  → {lib}")
            
        print("\n💡 FIX: Please run 'setup.bat' to install everything automatically.")
        print("!" * 60 + "\n")
        
        # Give them time to read before closing
        if sys.stdin.isatty():
            input("Press Enter to exit...")
        sys.exit(1)
        
    return True
