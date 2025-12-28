**RoamBuddy – AI Travel Chatbot**

RoamBuddy is a Generative AI–powered travel chatbot built to demonstrate end-to-end deployment of a large language model–backed application. The system integrates a Python backend, a conversational UI, and a persona-driven prompt design to deliver personalized travel planning assistance.

**Live Application:** 

https://roambuddy.ccbp.tech

**System Overview:**

RoamBuddy follows a simple request–response architecture:

- User submits a message via the chat interface
- Backend processes the input and applies persona context
- The request is forwarded to the LLM API
- The generated response is returned to the UI in real time
- The chatbot is conditioned with a predefined travel-guide persona to ensure consistent tone, style, and behavior across conversations.

**Persona Configuration:**

Arya – Virtual Travel Guide
Personality: Adventurous, street-smart, friendly
Response style: Practical, budget-aware, experience-focused
The persona is embedded at the prompt level to guide response tone and content.

**Technical Stack:**

Programming Language: Python
Frontend/UI: Gradio
LLM Provider: Google Gemini API
Model Used: gemini-2.5-flash
Deployment Platform: Hugging Face Spaces

**Local Setup & Execution:**

- Clone the repository
- Install dependencies:
pip install -r requirements.txt
- Run the application:
python app.py
- The application will be available at:
http://localhost:7860

**Known Limitations:**

API usage is subject to provider rate limits
Public access may lead to quota exhaustion on free tiers
No persistent conversation memory (stateless requests)

**Future Improvements:**

Long-term conversation memory
Model switching support (HF-hosted models)
User-specific travel personalization
Enhanced error handling and fallback responses
