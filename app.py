import os
import gradio as gr
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class TravelLLM:
    def __init__(self):
        self.memory_history = []

    def trim_text(self, text, max_chars=500):
        return text[:max_chars]

    def predict(self, user_message):
        # ✅ Shorter persona (prevents token overflow)
        system_prompt = (
            "You are Arya, a smart and friendly travel guide who gives practical, budget-friendly travel suggestions."
        )

        # ✅ Limit memory (VERY IMPORTANT)
        MAX_TURNS = 4
        self.memory_history = self.memory_history[-(MAX_TURNS * 2):]

        # Build messages
        messages = [{"role": "system", "content": system_prompt}]

        for role, content in self.memory_history:
            messages.append({
                "role": role,
                "content": self.trim_text(content)
            })

        messages.append({
            "role": "user",
            "content": self.trim_text(user_message)
        })

        # ✅ Final safety limit
        messages = messages[-10:]

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",   # ✅ correct syntax
                messages=messages
            )

            answer = response.choices[0].message.content

        except Exception as e:
            return f"Error: {str(e)}"

        # Update memory
        self.memory_history.append(("user", user_message))
        self.memory_history.append(("assistant", answer))

        return answer


llm_chain = TravelLLM()

def get_text_response(user_message, history):
    return llm_chain.predict(user_message)


demo = gr.ChatInterface(
    fn=get_text_response,
    examples=[
        "How are you doing?",
        "Plan a 3-day trip to Jaipur",
        "Suggest offbeat cafés in Delhi"
    ],
    title="Arya - Travel Guide ✈️",
    description="Your smart AI travel planner powered by Groq ⚡"
)

if __name__ == "__main__":
    demo.launch(debug=True)