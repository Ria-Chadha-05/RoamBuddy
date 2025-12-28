import os
import gradio as gr
from google import genai

"""**How to get Google Gemini API Key?**

- Go to https://aistudio.google.com/app/api-keys
- Click "Create API Key"
- Copy the API Key for your use
"""

GEMINI_API_KEY="AIzaSyBg1CYTTOfWBrOzgxBhBLqHjujx7qVurrM"
client = genai.Client(api_key=GEMINI_API_KEY)

"""
- Similar to Gemini Model we can also use HuggingFace Transformer Models.
- Reference links: https://python.langchain.com/docs/integrations/providers/huggingface , https://python.langchain.com/docs/integrations/llms/huggingface_hub.html

"""

# from langchain.llms import HuggingFacePipeline
# hf = HuggingFacePipeline.from_model_id(
#     model_id="gpt2",
#     task="text-generation",)

# Custom LLM wrapper for Gemini
class GeminiLLM:
    def __init__(self):
        self.memory_history = []

    def predict(self, user_message):
        # Persona prompt
        full_prompt = (
            "Meet Arya, your adventurous and street-smart travel guide! "
            "At 26 years old, Arya lives for exploring new places and uncovering hidden gems. "
            "With a backpack full of stories and a mind packed with travel hacks, Arya helps "
            "you plan stress-free, well-balanced itineraries tailored to your pace and budget. "
            "Whether it’s scenic cafés, local food spots, or offbeat experiences, Arya’s enthusiasm "
            "and practical tips make every trip feel exciting, personal, and perfectly planned.\n\n"
        )

        for msg in self.memory_history:
            full_prompt += msg + "\n"

        full_prompt += f"User: {user_message}\nArya:"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        answer = response.text

        # Update memory
        self.memory_history.append(f"User: {user_message}")
        self.memory_history.append(f"Arya: {answer}")

        # Keep last 10 turns
        if len(self.memory_history) > 20:
            self.memory_history = self.memory_history[-20:]

        return answer

llm_chain = GeminiLLM()

def get_text_response(user_message, history):
    return llm_chain.predict(user_message)

demo = gr.ChatInterface(
    get_text_response,
    examples=[
        "How are you doing?",
        "Plan a 3-day trip to Jaipur",
        "Suggest offbeat cafés in Delhi"
    ],
)

if __name__ == "__main__":
    demo.launch(debug=True) #To create a public link, set `share=True` in `launch()`. To enable errors and logs, set `debug=True` in `launch()`.
