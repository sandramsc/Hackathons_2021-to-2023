#!/usr/bin/env python3
"""
Test TTS and save audio file locally for playback
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from integrations.ibm_services import IBMServicesManager

def test_tts_save_local():
    """Test TTS and save audio file locally"""
    
    print("=" * 70)
    print("🎤 TTS Test - Save Audio Locally")
    print("=" * 70)
    
    # Initialize services
    print("\n📋 Initializing IBM Services...")
    services = IBMServicesManager()
    
    if not services.tts:
        print("❌ TTS service not initialized")
        return False
    
    print("✅ TTS service initialized")
    
    # Test text
    test_text = """Good morning. This is your ProActive CSI daily executive briefing.

Executive Summary: 4 critical customers requiring immediate attention. 
Total ARR at risk is $152,000. Two vendor delays are impacting customer satisfaction.

Top Risks: TechGlobal Inc with 85 percent churn risk, representing $78,000 in ARR at risk.
Acme Corp with 78 percent churn risk, representing $45,000 in ARR.

Voice briefing complete."""
    
    print(f"\n📋 Generating TTS Audio...")
    print(f"   Text: {len(test_text)} characters")
    
    # Generate audio
    result = services.synthesize_speech(
        text=test_text,
        output_path="test_executive_briefing.wav",
        upload_to_cloudant=False  # Just test TTS, skip Cloudant
    )
    
    if not result.get('success'):
        print(f"❌ TTS generation failed: {result.get('error')}")
        return False
    
    audio_size = len(result.get('audio_content', b''))
    file_path = Path("test_executive_briefing.wav")
    
    print(f"\n✅ Audio Generated Successfully")
    print(f"   Size: {audio_size:,} bytes")
    print(f"   Saved to: {file_path.absolute()}")
    
    if file_path.exists():
        print(f"   File exists: ✅")
        print(f"\n🔊 To play the audio:")
        print(f"   macOS: open {file_path}")
        print(f"   Linux: xdg-open {file_path}")
        print(f"   Or: Double-click the file in Finder/File Manager")
        
        # Try to open on macOS
        import platform
        if platform.system() == 'Darwin':
            import subprocess
            try:
                subprocess.run(['open', str(file_path)], check=True)
                print(f"\n✅ Opened audio file in default player")
            except:
                pass
    
    return True

if __name__ == "__main__":
    success = test_tts_save_local()
    if success:
        print("\n" + "=" * 70)
        print("✅ TEST COMPLETE - Audio file saved!")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("❌ TEST FAILED")
        print("=" * 70)
        sys.exit(1)

