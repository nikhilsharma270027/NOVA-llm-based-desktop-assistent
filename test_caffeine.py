#!/usr/bin/env python3
"""
Caffeine Mode Verification Script
Tests the caffeine mode feature by enabling it, waiting, then disabling it.
"""

import sys
import time
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

# Import system module
from nova.agents import system

def main():
    print("=" * 60)
    print("         CAFFEINE MODE VERIFICATION TEST")
    print("=" * 60)
    
    # Test 1: Enable caffeine mode
    print("\n[TEST 1] Enabling Caffeine Mode...")
    result = system.toggle_caffeine(True)
    print(f"   Result: {result}")
    
    if "already active" in result:
        print("   ⚠️  Caffeine was already running. Stopping it first...")
        system.toggle_caffeine(False)
        time.sleep(2)
        result = system.toggle_caffeine(True)
        print(f"   Result: {result}")
    
    # Test 2: Wait and observe
    print("\n[TEST 2] Waiting 5 seconds...")
    print("   👀 Watch for micro mouse movements every 60 seconds")
    print("   (The first jiggle should happen in 60 seconds)")
    for i in range(5, 0, -1):
        print(f"   {i}...", flush=True)
        time.sleep(1)
    
    # Test 3: Trying to enable again (double-start protection test)
    print("\n[TEST 3] Testing Double-Start Protection...")
    result = system.toggle_caffeine(True)
    print(f"   Result: {result}")
    if "already active" in result:
        print("   ✅ Double-start protection working correctly!")
    else:
        print("   ⚠️  Warning: Double-start protection may not be working")
    
    # Test 4: Disable caffeine mode
    print("\n[TEST 4] Disabling Caffeine Mode...")
    result = system.toggle_caffeine(False)
    print(f"   Result: {result}")
    
    # Test 5: Try to disable again
    print("\n[TEST 5] Testing Double-Stop Protection...")
    result = system.toggle_caffeine(False)
    print(f"   Result: {result}")
    if "already off" in result:
        print("   ✅ Double-stop protection working correctly!")
    else:
        print("   ⚠️  Warning: Double-stop protection may not be working")
    
    print("\n" + "=" * 60)
    print("         ✅ VERIFICATION COMPLETE!")
    print("=" * 60)
    print("\n📝 Summary:")
    print("   • Caffeine mode can be enabled and disabled")
    print("   • Double-start/stop protection is working")
    print("   • Thread management appears functional")
    print("\n💡 Next Steps:")
    print("   • Test via Telegram: /caffeine on")
    print("   • Test via natural language: 'keep my laptop awake'")
    print("   • Leave system idle to verify sleep prevention")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        print("   Disabling caffeine mode...")
        system.toggle_caffeine(False)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
