#!/usr/bin/env python3
"""
Test script for /find text search functionality
"""
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from nova.features.files.finder import search_files_by_content

def test_search():
    # Test searching for "find me nova" in Desktop
    search_text = "find me nova"
    
    print(f"\n🔍 Testing search for: '{search_text}'")
    print("=" * 60)
    
    result = search_files_by_content(search_text)
    
    print(f"\nStatus: {result.get('status')}")
    print(f"Message: {result.get('message')}")
    
    if result.get('status') == 'found':
        files = result.get('files', [])
        print(f"\n✅ Found {len(files)} file(s):")
        
        for file_info in files:
            print(f"\n  📄 {file_info['file_name']}")
            print(f"     Type: {file_info['file_type']}")
            print(f"     Size: {file_info['file_size_mb']:.2f} MB")
            print(f"     Matches: {file_info['matches_count']}")
            
            if file_info['matches']:
                print(f"     First match:")
                for match in file_info['matches'][:2]:
                    print(f"       Line {match['line_number']}: {match['line_content']}")
    else:
        print(f"\n❌ {result.get('message')}")
        print("\n📂 Checking Desktop folder...")
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop):
            files = os.listdir(desktop)
            print(f"Files in Desktop: {len(files)}")
            for f in files[:10]:
                print(f"   - {f}")
        else:
            print(f"Desktop not found at: {desktop}")

if __name__ == "__main__":
    test_search()
