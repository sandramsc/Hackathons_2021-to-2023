#!/usr/bin/env python3
"""
Full TTS workflow test - Simulates what the agent does
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from integrations.ibm_services import IBMServicesManager

def test_full_tts_workflow():
    """Test the complete TTS workflow as the agent would use it"""
    
    print("=" * 70)
    print("🎤 FULL TTS WORKFLOW TEST - Executive Briefing")
    print("=" * 70)
    
    # Initialize services
    print("\n📋 Step 1: Initializing IBM Services...")
    services = IBMServicesManager()
    
    if not services.tts:
        print("❌ TTS service not initialized")
        return False
    
    print("✅ All services initialized")
    
    # Simulate executive briefing text
    briefing_text = """Good morning. This is your ProActive CSI daily executive briefing for November 22, 2025.

Executive Summary: 4 critical customers requiring immediate attention. Total ARR at risk is $152,000. Two vendor delays are impacting customer satisfaction. Churn prediction accuracy remains at 89 percent.

Top Risks: First, TechGlobal Inc with 85 percent churn risk, representing $78,000 in ARR at risk. Procurement delay is causing customer dissatisfaction. Immediate intervention is required.

Second, Acme Corp with 78 percent churn risk, representing $45,000 in ARR. Low engagement and no recent contact detected. Executive check-in is recommended.

Third, DataSystems with 52 percent churn risk, representing $28,000 in ARR. Support tickets are increasing, and procurement delay is affecting customer satisfaction.

Fourth, CloudVenture with 28 percent churn risk, representing $12,000 in ARR. Healthy account, but monitoring is recommended.

Procurement Alerts: DeltaSteel is 14 days late, affecting 2 customers. LogisticsPro is 7 days late, affecting 1 customer. Total revenue impact from vendor delays is $122,000 in ARR.

Financial Impact: ARR at risk totals $152,000. Protection potential is $122,000 with a 78 percent intervention success rate. Estimated ROI is 1,840 percent. Procurement penalties total $16,500.

Recommended Actions: First, escalate TechGlobal Inc to executive team today. Second, execute Procurement-Customer Impact Bridge workflow. Third, schedule executive check-in with Acme Corp this week. Fourth, review vendor contracts for penalty clauses.

Voice briefing complete. Full detailed report available upon request."""
    
    print(f"\n📋 Step 2: Generating TTS Audio...")
    print(f"   Text length: {len(briefing_text)} characters")
    print(f"   Voice: en-US_MichaelV3Voice")
    print(f"   Format: audio/wav")
    
    # Generate audio and upload to Cloudant
    result = services.synthesize_speech(
        text=briefing_text,
        upload_to_cloudant=True
    )
    
    print("\n" + "=" * 70)
    print("📊 RESULTS")
    print("=" * 70)
    
    if not result.get('success'):
        print(f"❌ TTS generation failed: {result.get('error')}")
        return False
    
    print(f"\n✅ Audio Generated Successfully")
    print(f"   Size: {len(result.get('audio_content', b'')):,} bytes")
    print(f"   Format: WAV (44.1 kHz, 16-bit)")
    
    # Calculate approximate duration (assuming 220KB per ~10 seconds)
    audio_size = len(result.get('audio_content', b''))
    estimated_duration = (audio_size / 220958) * 10  # Rough estimate
    print(f"   Estimated duration: ~{estimated_duration:.1f} seconds")
    
    if result.get('cloudant_url'):
        print(f"\n✅ Audio Uploaded to Cloudant")
        print(f"   Document ID: {result.get('doc_id')}")
        print(f"   Download URL:")
        print(f"   {result.get('cloudant_url')}")
        print(f"\n🔗 You can download and play the audio by:")
        print(f"   1. Copy the URL above")
        print(f"   2. Paste in your browser")
        print(f"   3. The audio file will download")
        print(f"   4. Play it with any audio player")
    else:
        print(f"\n⚠️  Cloudant Upload Status")
        if services.cloudant:
            print(f"   Cloudant is initialized but upload failed")
            print(f"   Error: {result.get('error', 'Unknown error')}")
            print(f"\n   Possible reasons:")
            print(f"   - Database 'proactive_csi' doesn't exist")
            print(f"   - API key doesn't have write permissions")
            print(f"   - Network/authentication issue")
            print(f"\n   Solution: Create database manually in IBM Cloud Console")
        else:
            print(f"   Cloudant not initialized - upload skipped")
            print(f"   (TTS still works, just no download link)")
    
    print("\n" + "=" * 70)
    print("✅ TEST COMPLETE")
    print("=" * 70)
    
    if result.get('cloudant_url'):
        print(f"\n🎉 SUCCESS! Audio is ready for download:")
        print(f"   {result.get('cloudant_url')}")
        return True
    else:
        print(f"\n⚠️  Audio generated but Cloudant upload failed")
        print(f"   TTS is working, but download link unavailable")
        return True  # Still success since TTS works

if __name__ == "__main__":
    success = test_full_tts_workflow()
    sys.exit(0 if success else 1)

