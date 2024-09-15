import streamlit as st
import re

with st.sidebar:
    st.header("My Amazing App🤞")
    st.markdown("""
                Welcome to my awesome app❤
                Feel free to visit my website:
                - [BenziRaz](http://localhost:8501)
                """)
    

def main():
    st.header("Text Analyzer🐵")

    file = st.file_uploader("Upload your file here: ", type=".txt")

    if file:
        question = st.chat_input("Ask anything about your file:")
        if question:
            message = st.chat_message("user")
            message.write(question)

            prompt = {
                "question": question,
                "document": file.read().decode("utf-8"),
                "size": len(file.read())
            }


            text_pattern = re.compile(r"רשום|טקסט")
            size_pattern = re.compile(r"מידה")

            assistant_message = st.chat_message("ai")

            if text_pattern.search(question):
                assistant_message.write(prompt["document"])
            elif size_pattern.search(question):
                assistant_message.write(f"{prompt["size"] / 1000 if prompt['size'] > 1000 else prompt['size']}kb")
            else: 
                assistant_message.write("Invalid message, how can I help you?")


if __name__ == "__main__":
    main()