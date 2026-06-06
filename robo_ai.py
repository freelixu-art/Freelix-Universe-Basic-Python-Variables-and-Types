import pyttsx3
import speech_recognition as sr
import openai
import datetime
import os

# Initialize Text-to-Speech Engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Initialize OpenAI API Key
openai.api_key = "your-openai-api-key"

# Function to recognize voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I assist you?")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            return command.lower()
        except sr.RequestError:
            speak("I'm unable to connect to the service. Please check your internet connection.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Can you repeat?")
            return ""

# Function to interact with OpenAI for intelligent responses
def respond_with_ai(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion["choices"][0]["message"]["content"]
        print(response)
        speak(response)
    except Exception as e:
        print(f"Error with AI response: {e}")
        speak("I encountered a problem. Please try again later.")

# Main function of Robo AI
def robo_ai():
    speak("Robo AI initialized. Welcome back. What can I do for you?")
    while True:
        command = take_command()

        # General Commands
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}.")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")

        elif "open browser" in command:
            speak("Opening your web browser.")
            os.system("start chrome")  # Replace with your preferred browser

        elif "search" in command:
            prompt = command.replace("search", "")
            respond_with_ai(prompt)

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            respond_with_ai(command)

if __name__ == "__main__":
    robo_ai()