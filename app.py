import streamlit as st
from ollama import chat

st.set_page_config(
    page_title="AI Prompt Optimizer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Prompt Optimizer")

st.write("Convert simple prompts into professional AI prompts.")

user_prompt = st.text_area(
    "Enter your prompt",
    height=150
)

if st.button("Optimize Prompt"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:

        system_prompt = f"""
You are an expert Prompt Engineer.

Convert the following user request into
a professional, detailed, structured prompt.

User Request:
{user_prompt}
"""

        with st.spinner("Optimizing..."):

            response = chat(
                model="phi3:mini",
                messages=[
                    {
                        "role": "user",
                        "content": system_prompt
                    }
                ]
            )

        st.success("Optimized Prompt")

        st.text_area(
            "Result",
            response["message"]["content"],
            height=300
        )