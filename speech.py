import speech_recognition as sr
from pynput.keyboard import Controller, Key
import time

def speech_to_text():
    """Utilise le micro pour transcrire la parole en texte."""

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Parlez maintenant...")
        try:
            audio = r.listen(source, phrase_time_limit=5)  # Écoute pendant 5 secondes
        except sr.WaitTimeoutError:
             print("Délai dépassé. Aucun son détecté")
             return None
        print("Reconnaissance en cours...")

    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("Vous avez dit: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas compris l'audio")
        return None
    except sr.RequestError as e:
        print(f"Erreur lors de la demande au service Google Speech Recognition; {e}")
        return None

def write_text(text):
    """Utilise pynput pour simuler la saisie du texte."""
    keyboard = Controller()
    keyboard.type(text)

def main():
    print("Programme de transcription vocale et de saisie lancé. Fermer la fenêtre ou appuyer sur Ctrl+C pour arrêter.")
    
    while True:
        text = speech_to_text()
        if text:
            write_text(text)
            keyboard = Controller()
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(0.5) # Pause de 0.5 seconde pour éviter une trop grande sollicitation du processeur
        
if __name__ == "__main__":
    main()