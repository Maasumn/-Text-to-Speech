import pyttsx3

def text_to_audio(text, filename='audio.mp3'):
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print(f"Audio file saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    text = input("Enter the text you want to convert to audio: ")
    text_to_audio(text)
