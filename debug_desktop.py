#!/usr/bin/env python3
"""
Debug script to check Desktop files
"""
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

print(f"\n📂 Desktop folder: {desktop}")
print(f"✅ Exists: {os.path.exists(desktop)}\n")

if os.path.exists(desktop):
    print("📋 Files on Desktop:")
    print("=" * 60)
    
    files = os.listdir(desktop)
    print(f"Total files: {len(files)}\n")
    
    for filename in files:
        file_path = os.path.join(desktop, filename)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"  📄 {filename} ({size} bytes)")
            
            # Try to read and show first 5 lines
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()[:5]
                    if "find me nova" in open(file_path, 'r', encoding='utf-8', errors='ignore').read().lower():
                        print(f"     ✅ Contains 'find me nova'")
                        for i, line in enumerate(lines, 1):
                            print(f"       Line {i}: {line.strip()[:60]}")
            except:
                pass
        print()
