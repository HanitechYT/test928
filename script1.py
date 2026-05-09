from openai import OpenAI
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Simple AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# OpenAI client
client = OpenAI(api_key="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")

# App title
st.title("🤖 Simple AI Assistant")
st.write("اكتب سؤالك، والمساعد رح يجاوبك مباشرة.")

# Input box
user_question = st.text_area("اكتب سؤالك هنا:", height=120)

# Button
if st.button("اسأل المساعد 🚀"):

    if user_question.strip() == "":
        st.warning("اكتب سؤال أولاً.")
    else:
        with st.spinner("عم يفكر..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": user_question}
                ]
            )

            answer = response.choices[0].message.content

        st.success("تمت الإجابة ✅")
        st.markdown("### الجواب:")
        st.write(answer)