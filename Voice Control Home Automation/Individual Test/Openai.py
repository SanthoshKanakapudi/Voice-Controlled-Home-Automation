#API Key is invalid now
import openai
import speech_recognition as sr
import pyttsx3

# Initialize OpenAI API
# Risk Free...
openai.api_key = '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' 
 # Replace with your actual OpenAI API key

# Initialize the speech recognition and TTS engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_to_speech():
    """Capture speech from the microphone and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def get_chatgpt_response(prompt):
    """Send the recognized text to ChatGPT and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        message = response.choices[0].message['content'].strip()
        print(f"ChatGPT says: {message}")
        return message
    except openai.error.InvalidRequestError as e:
        print("Invalid Request: ", e)
        return "There was an issue with your request. Please try again."
    except openai.error.RateLimitError as e:
        print("Rate Limit Exceeded: ", e)
        return "Rate limit exceeded. Please wait and try again later."
    except openai.error.AuthenticationError:
        return "Authentication error. Please check your API key."
    except Exception as e:
        print(f"Error while communicating with ChatGPT: {e}")
        return "I'm sorry, I encountered an issue while processing your request."


def speak_text(text):
    """Convert text to speech and play it."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Main loop
while True:
    print("Say 'stop' to end the program.")
    spoken_text = listen_to_speech()
    
    if spoken_text:
        if "stop" in spoken_text.lower():
            print("Stopping program.")
            break
        
        # Get the response from ChatGPT
        response_text = get_chatgpt_response(spoken_text)
        
        # Speak out the response
        speak_text(response_text)
