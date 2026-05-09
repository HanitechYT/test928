from openai import OpenAI
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Simple AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
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
