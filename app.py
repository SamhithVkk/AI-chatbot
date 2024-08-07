import streamlit as st
import speech_recognition as sr
from agent import run_conversation

def main():
    st.title("JARVIS Chatbot")
    st.write("Type your message or use voice input to interact with JARVIS.")

    # Text input section
    user_input = st.text_input("Enter your message here:")

    if st.button("Send"):
        if user_input.strip() != "":
            st.write("You: " + user_input)
            response = run_conversation(user_input)
            st.write("JARVIS: " + response)

    # Voice input section
    if st.button("Start Listening"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            st.write("Recognizing...")
            try:
                transcript = recognizer.recognize_google(audio)
                st.write("You: " + transcript)
                response = run_conversation(transcript)
                st.write("JARVIS: " + response)
            except sr.UnknownValueError:
                st.write("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                st.write(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
