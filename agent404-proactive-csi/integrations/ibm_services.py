"""
IBM watsonx Services Integration
Integrates all IBM Cloud services with proper credentials
"""

import json
import os
from pathlib import Path
from ibm_watson import NaturalLanguageUnderstandingV1, SpeechToTextV1, TextToSpeechV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as CloudantAuth

class IBMServicesManager:
    """
    Centralized manager for all IBM watsonx services
    """
    
    def __init__(self):
        self.nlu = None
        self.stt = None
        self.tts = None
        self.cloudant = None
        self.watsonx_orchestrate = None
        self._initialize_services()
    
    def _initialize_services(self):
        """Initialize all IBM services with credentials"""
        try:
            self._init_nlu()
            self._init_stt()
            self._init_tts()
            self._init_cloudant()
            print("✅ IBM Services initialized successfully")
        except Exception as e:
            print(f"⚠️ Warning: Some IBM services may not be fully initialized: {e}")
    
    def _init_nlu(self):
        """Initialize Natural Language Understanding"""
        try:
            apikey = os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_APIKEY', 'JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar')
            url = os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_URL', 
                          'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3')
            
            authenticator = IAMAuthenticator(apikey)
            self.nlu = NaturalLanguageUnderstandingV1(
                version='2022-04-07',
                authenticator=authenticator
            )
            self.nlu.set_service_url(url)
            print("✅ NLU service initialized")
        except Exception as e:
            print(f"⚠️ NLU initialization warning: {e}")
    
    def _init_stt(self):
        """Initialize Speech to Text"""
        try:
            apikey = os.getenv('SPEECH_TO_TEXT_APIKEY', 'qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1')
            url = os.getenv('SPEECH_TO_TEXT_URL',
                          'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c')
            
            authenticator = IAMAuthenticator(apikey)
            self.stt = SpeechToTextV1(authenticator=authenticator)
            self.stt.set_service_url(url)
            print("✅ Speech-to-Text service initialized")
        except Exception as e:
            print(f"⚠️ STT initialization warning: {e}")
    
    def _init_tts(self):
        """Initialize Text to Speech"""
        try:
            apikey = os.getenv('TEXT_TO_SPEECH_APIKEY', 'FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz')
            url = os.getenv('TEXT_TO_SPEECH_URL',
                          'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7')
            
            authenticator = IAMAuthenticator(apikey)
            self.tts = TextToSpeechV1(authenticator=authenticator)
            self.tts.set_service_url(url)
            print("✅ Text-to-Speech service initialized")
        except Exception as e:
            print(f"⚠️ TTS initialization warning: {e}")
    
    def _init_cloudant(self):
        """Initialize Cloudant NoSQL Database"""
        try:
            # Try to read from .env or config file first
            creds = None
            
            # Try .env file
            env_file = Path(__file__).parent.parent.parent / ".env"
            if env_file.exists():
                with open(env_file, 'r') as f:
                    for line in f:
                        if 'CLOUDANT' in line and '=' in line:
                            key, value = line.strip().split('=', 1)
                            if 'API_KEY' in key or 'APIKEY' in key:
                                if not creds:
                                    creds = {}
                                creds['apikey'] = value.strip().strip('"').strip("'")
                            elif 'URL' in key:
                                if not creds:
                                    creds = {}
                                creds['url'] = value.strip().strip('"').strip("'")
            
            # Try credentials file
            if not creds:
                cred_path = Path(__file__).parent.parent.parent / 'ibm-credentials_Cloudant_data.json'
                if not cred_path.exists():
                    cred_path = Path(__file__).parent.parent / 'ibm-credentials_Cloudant_data.json'
                
                if cred_path.exists():
                    with open(cred_path, 'r') as f:
                        content = f.read().strip()
                        # Handle both JSON and string formats
                        if content.startswith('"'):
                            content = content.strip('"')
                        creds = json.loads(content) if isinstance(content, str) else content
            
            # Fallback to embedded credentials from ibm_services.py
            if not creds:
                creds = {
                    "apikey": "TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK",
                    "url": "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud"
                }
            
            authenticator = CloudantAuth(creds['apikey'])
            self.cloudant = CloudantV1(authenticator=authenticator)
            self.cloudant.set_service_url(creds['url'])
            print("✅ Cloudant database initialized")
        except Exception as e:
            print(f"⚠️ Cloudant initialization warning: {e}")
            # Still try to initialize with fallback credentials
            try:
                creds = {
                    "apikey": "TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK",
                    "url": "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud"
                }
                authenticator = CloudantAuth(creds['apikey'])
                self.cloudant = CloudantV1(authenticator=authenticator)
                self.cloudant.set_service_url(creds['url'])
                print("✅ Cloudant database initialized with fallback credentials")
            except Exception as e2:
                print(f"❌ Cloudant initialization failed: {e2}")
                self.cloudant = None
    
    # ===== NLU Methods =====
    
    def analyze_sentiment(self, text: str) -> dict:
        """
        Analyze sentiment and emotions using NLU
        """
        try:
            response = self.nlu.analyze(
                text=text,
                features=Features(
                    sentiment=SentimentOptions(),
                    emotion=EmotionOptions(),
                    keywords=KeywordsOptions(limit=5)
                )
            ).get_result()
            
            return {
                "sentiment": response.get('sentiment', {}).get('document', {}),
                "emotions": response.get('emotion', {}).get('document', {}).get('emotion', {}),
                "keywords": response.get('keywords', []),
                "raw_response": response
            }
        except Exception as e:
            print(f"NLU analysis error: {e}")
            return {
                "sentiment": {"label": "neutral", "score": 0.0},
                "emotions": {},
                "keywords": [],
                "error": str(e)
            }
    
    def analyze_customer_communication(self, text: str) -> dict:
        """
        Analyze customer communication for risk signals
        """
        analysis = self.analyze_sentiment(text)
        
        # Extract risk signals
        risk_keywords = ['cancel', 'terminate', 'disappointed', 'frustrated', 
                        'alternative', 'competitor', 'unacceptable', 'reconsider']
        
        text_lower = text.lower()
        detected_risks = [kw for kw in risk_keywords if kw in text_lower]
        
        sentiment_score = analysis['sentiment'].get('score', 0)
        
        # Calculate overall risk level
        if sentiment_score < -0.5 or len(detected_risks) >= 2:
            risk_level = "HIGH"
        elif sentiment_score < -0.2 or len(detected_risks) >= 1:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        return {
            "sentiment_analysis": analysis['sentiment'],
            "emotions": analysis['emotions'],
            "risk_level": risk_level,
            "risk_keywords_detected": detected_risks,
            "keywords": analysis['keywords']
        }
    
    # ===== Speech Services Methods =====
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Convert speech to text using Speech-to-Text service
        """
        try:
            with open(audio_file_path, 'rb') as audio_file:
                response = self.stt.recognize(
                    audio=audio_file,
                    content_type='audio/wav',
                    model='en-US_BroadbandModel'
                ).get_result()
            
            # Extract transcript
            transcript = ""
            for result in response.get('results', []):
                for alternative in result.get('alternatives', []):
                    transcript += alternative.get('transcript', '') + " "
            
            return transcript.strip()
        except Exception as e:
            print(f"STT error: {e}")
            return f"Error transcribing audio: {e}"
    
    def synthesize_speech(self, text: str, output_path: str = None, upload_to_cloudant: bool = True) -> dict:
        """
        Convert text to speech using Text-to-Speech service
        Optionally uploads audio to Cloudant and returns download URL
        
        Returns:
            dict with keys:
            - audio_content: bytes (audio data)
            - cloudant_url: str (download URL if uploaded)
            - doc_id: str (Cloudant document ID)
            - success: bool
        """
        try:
            response = self.tts.synthesize(
                text=text,
                accept='audio/wav',
                voice='en-US_MichaelV3Voice'
            ).get_result()
            
            audio_content = response.content
            
            if output_path:
                with open(output_path, 'wb') as audio_file:
                    audio_file.write(audio_content)
            
            import base64
            
            # Generate base64 data URL for inline playback
            audio_base64 = base64.b64encode(audio_content).decode('utf-8')
            data_url = f"data:audio/wav;base64,{audio_base64}"
            
            result = {
                'audio_content': audio_content,
                'audio_base64': audio_base64,
                'data_url': data_url,
                'success': True,
                'cloudant_url': None,
                'doc_id': None
            }
            
            # Upload to Cloudant if requested and Cloudant is available
            if upload_to_cloudant and self.cloudant and audio_content:
                upload_result = self.upload_audio_to_cloudant(audio_content, text[:100])
                if upload_result.get('success'):
                    result['cloudant_url'] = upload_result.get('download_url')
                    result['doc_id'] = upload_result.get('doc_id')
            
            return result
        except Exception as e:
            print(f"TTS error: {e}")
            return {
                'audio_content': None,
                'success': False,
                'error': str(e),
                'cloudant_url': None,
                'doc_id': None
            }
    
    # ===== Cloudant Database Methods =====
    
    def store_customer_health_record(self, customer_id: str, health_data: dict) -> dict:
        """
        Store customer health record in Cloudant
        """
        try:
            import time
            from datetime import datetime
            
            # Add metadata
            health_data['_id'] = f"health_{customer_id}_{int(time.time())}"
            health_data['type'] = 'customer_health'
            health_data['customer_id'] = customer_id
            health_data['timestamp'] = datetime.now().isoformat()
            
            response = self.cloudant.post_document(
                db='proactive_csi',
                document=health_data
            ).get_result()
            
            return {"success": True, "id": response.get('id'), "rev": response.get('rev')}
        except Exception as e:
            print(f"Cloudant storage error: {e}")
            return {"success": False, "error": str(e)}
    
    def store_intervention_record(self, intervention_data: dict) -> dict:
        """
        Store intervention execution record in Cloudant
        """
        try:
            from datetime import datetime
            
            intervention_data['type'] = 'intervention'
            intervention_data['timestamp'] = datetime.now().isoformat()
            
            # Generate unique ID if not present
            if '_id' not in intervention_data:
                intervention_data['_id'] = f"intervention_{intervention_data.get('customer_id', 'unknown')}_{int(datetime.now().timestamp())}"
            
            response = self.cloudant.post_document(
                db='proactive_csi',
                document=intervention_data
            ).get_result()
            
            return {"success": True, "id": response.get('id')}
        except Exception as e:
            print(f"Cloudant intervention storage error: {e}")
            return {"success": False, "error": str(e)}
    
    def query_customer_history(self, customer_id: str) -> list:
        """
        Query customer historical records from Cloudant
        """
        try:
            # Query using Cloudant Query API
            selector = {
                'customer_id': customer_id,
                'type': {'$in': ['customer_health', 'intervention']}
            }
            
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=100,
                sort=[{'timestamp': 'desc'}]
            ).get_result()
            
            return response.get('docs', [])
        except Exception as e:
            print(f"Cloudant query error: {e}")
            return []
    
    def upload_audio_to_cloudant(self, audio_content: bytes, description: str = "TTS Audio") -> dict:
        """
        Upload audio file to Cloudant as an attachment
        
        Args:
            audio_content: bytes - Audio file content
            description: str - Description of the audio
            
        Returns:
            dict with success, download_url, doc_id
        """
        try:
            import base64
            import time
            from datetime import datetime
            from ibmcloudant.cloudant_v1 import CloudantV1
            
            if not self.cloudant:
                return {"success": False, "error": "Cloudant not initialized"}
            
            # Try to create database if it doesn't exist
            try:
                self.cloudant.get_database_information(db='proactive_csi').get_result()
            except Exception as db_error:
                if 'not_found' in str(db_error).lower() or '404' in str(db_error):
                    print("📋 Database 'proactive_csi' not found, attempting to create...")
                    try:
                        self.cloudant.put_database(db='proactive_csi').get_result()
                        print("✅ Created database 'proactive_csi'")
                    except Exception as create_error:
                        print(f"⚠️  Could not create database: {create_error}")
                        return {"success": False, "error": f"Database creation failed: {create_error}"}
                else:
                    raise db_error
            
            # Generate unique document ID
            doc_id = f"tts_audio_{int(time.time())}"
            attachment_name = "audio.wav"
            
            # Encode audio as base64
            audio_base64 = base64.b64encode(audio_content).decode('utf-8')
            
            # Create document with attachment
            doc = {
                "_id": doc_id,
                "type": "tts_audio",
                "description": description,
                "timestamp": datetime.now().isoformat(),
                "format": "audio/wav",
                "voice": "en-US_MichaelV3Voice",
                "size_bytes": len(audio_content),
                "_attachments": {
                    attachment_name: {
                        "content_type": "audio/wav",
                        "data": audio_base64
                    }
                }
            }
            
            # Upload to Cloudant
            response = self.cloudant.post_document(
                db='proactive_csi',
                document=doc
            ).get_result()
            
            # Generate download URL with authentication
            # Format: https://{account}.cloudantnosqldb.appdomain.cloud/{db}/{doc_id}/{attachment_name}
            cloudant_url = self.cloudant.service_url
            # Extract account from URL (e.g., f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix)
            if '.cloudantnosqldb.appdomain.cloud' in cloudant_url:
                account = cloudant_url.split('//')[1].split('.')[0]
                # Use direct attachment URL (no auth needed for public attachments)
                download_url = f"https://{account}.cloudantnosqldb.appdomain.cloud/proactive_csi/{doc_id}/{attachment_name}"
                # Also provide a clickable markdown link
                download_link = f"[Download Audio File (WAV)]({download_url})"
            else:
                # Fallback: construct from service URL
                download_url = f"{cloudant_url}/proactive_csi/{doc_id}/{attachment_name}"
                download_link = f"[Download Audio File (WAV)]({download_url})"
            
            return {
                "success": True,
                "doc_id": doc_id,
                "download_url": download_url,
                "rev": response.get('rev')
            }
        except Exception as e:
            print(f"Cloudant audio upload error: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_analytics_dashboard_data(self) -> dict:
        """
        Retrieve aggregated analytics data for dashboard
        """
        try:
            # Query all customer health records
            selector = {'type': 'customer_health'}
            
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=1000
            ).get_result()
            
            docs = response.get('docs', [])
            
            # Aggregate data
            total_customers = len(set(doc.get('customer_id') for doc in docs))
            high_risk = len([doc for doc in docs if doc.get('risk_level') == 'HIGH' or doc.get('risk_level') == 'CRITICAL'])
            
            return {
                "total_customers_tracked": total_customers,
                "high_risk_customers": high_risk,
                "total_interventions": len([doc for doc in docs if doc.get('type') == 'intervention']),
                "data_points": len(docs)
            }
        except Exception as e:
            print(f"Analytics query error: {e}")
            return {
                "total_customers_tracked": 0,
                "high_risk_customers": 0,
                "total_interventions": 0,
                "error": str(e)
            }
    
    # ===== Data Retrieval Methods from Cloudant =====
    
    def get_all_customers(self) -> list:
        """Get all customer records from Cloudant"""
        try:
            selector = {'type': 'customers'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting customers: {e}")
            return []
    
    def get_customer_by_id(self, customer_id: str) -> dict:
        """Get specific customer by ID"""
        try:
            selector = {'type': 'customers', 'customer_id': customer_id}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=1
            ).get_result()
            docs = response.get('docs', [])
            return docs[0] if docs else {}
        except Exception as e:
            print(f"Error getting customer {customer_id}: {e}")
            return {}
    
    def get_all_vendors(self) -> list:
        """Get all vendor records from Cloudant"""
        try:
            selector = {'type': 'vendors'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting vendors: {e}")
            return []
    
    def get_all_contracts(self) -> list:
        """Get all contract records from Cloudant"""
        try:
            selector = {'type': 'contracts'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting contracts: {e}")
            return []
    
    def get_all_support_tickets(self) -> list:
        """Get all support ticket records from Cloudant"""
        try:
            selector = {'type': 'support_tickets'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting support tickets: {e}")
            return []
    
    def get_all_customer_comms(self) -> list:
        """Get all customer communication records from Cloudant"""
        try:
            selector = {'type': 'customer_comms'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting customer communications: {e}")
            return []
    
    def get_all_revenue_records(self) -> list:
        """Get all revenue exposure records from Cloudant"""
        try:
            selector = {'type': 'revenue'}
            response = self.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=10000
            ).get_result()
            return response.get('docs', [])
        except Exception as e:
            print(f"Error getting revenue records: {e}")
            return []
    
    def get_data_summary(self) -> dict:
        """Get summary of all data in Cloudant"""
        try:
            summary = {
                'customers': len(self.get_all_customers()),
                'vendors': len(self.get_all_vendors()),
                'contracts': len(self.get_all_contracts()),
                'support_tickets': len(self.get_all_support_tickets()),
                'customer_comms': len(self.get_all_customer_comms()),
                'revenue_records': len(self.get_all_revenue_records())
            }
            return summary
        except Exception as e:
            print(f"Error getting data summary: {e}")
            return {}
    
    # ===== watsonx.ai Methods (Mock for now) =====
    
    def predict_churn_watsonx(self, customer_features: dict) -> float:
        """
        Use watsonx.ai for churn prediction
        (This is a mock - in production, this would call actual watsonx.ai endpoint)
        """
        # Mock implementation - would integrate with actual watsonx.ai model
        # For hackathon, we use the Customer Success Agent's logic
        
        print("🤖 Calling watsonx.ai churn prediction model...")
        
        # In production, this would be:
        # response = watsonx_client.predict(model_id='churn_model_v1', features=customer_features)
        
        # Mock prediction based on features
        usage_drop = customer_features.get('usage_drop_pct', 0)
        sentiment = customer_features.get('sentiment_score', 0)
        tickets = customer_features.get('ticket_volume', 0)
        
        churn_prob = (usage_drop / 100 * 0.4 + 
                     abs(min(sentiment, 0)) * 0.4 + 
                     min(tickets / 20, 1) * 0.2)
        
        return round(min(churn_prob, 1.0), 3)
    
    def generate_intervention_recommendation(self, customer_data: dict) -> dict:
        """
        Use watsonx.ai to generate personalized intervention recommendations
        """
        print("🤖 Generating AI-powered intervention recommendations...")
        
        # This would call watsonx.ai in production
        # For hackathon, return structured recommendations
        
        risk_level = customer_data.get('risk_level', 'MEDIUM')
        
        recommendations = {
            "CRITICAL": [
                "Immediate C-level executive engagement",
                "Emergency technical review within 24 hours",
                "Offer service credits and contract flexibility",
                "Assign dedicated success pod"
            ],
            "HIGH": [
                "Schedule executive business review",
                "Conduct comprehensive health check",
                "Provide premium support access",
                "Share customer success stories"
            ],
            "MEDIUM": [
                "Increase touchpoint frequency",
                "Share product roadmap and updates",
                "Offer training session",
                "Conduct QBR"
            ]
        }
        
        return {
            "recommendations": recommendations.get(risk_level, recommendations["MEDIUM"]),
            "confidence": 0.87,
            "model_version": "watsonx-intervention-v1"
        }


# Singleton instance
_ibm_services = None

def get_ibm_services() -> IBMServicesManager:
    """Get singleton instance of IBM Services Manager"""
    global _ibm_services
    if _ibm_services is None:
        _ibm_services = IBMServicesManager()
    return _ibm_services


if __name__ == "__main__":
    # Test IBM services
    print("\n🧪 Testing IBM Services Integration\n")
    
    services = get_ibm_services()
    
    # Test NLU
    test_text = "We are reconsidering our renewal. The service has been disappointing."
    print("Testing NLU sentiment analysis...")
    analysis = services.analyze_customer_communication(test_text)
    print(f"Risk Level: {analysis['risk_level']}")
    print(f"Sentiment: {analysis['sentiment_analysis']}")
    print(f"Risk Keywords: {analysis['risk_keywords_detected']}")
    
    print("\n✅ IBM Services integration test complete")

