import RPi.GPIO as GPIO
import speech_recognition as sr
import time

class App():
    def __init__(self):
        # Set up GPIO mode
        GPIO.setmode(GPIO.BOARD)
        
        self.led = 11

        # Set up GPIO pin for LED
        GPIO.setup(self.led, GPIO.OUT)

        # Create a speech recognition object
        r = sr.Recognizer()
    
    def start(self):
        while True:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

            # Try to recognize the speech
            try:
                command = r.recognize_google(audio)
                print("You said: " + command)

                # Check if the command is to turn the LED on or off
                if "on" in command.lower():
                    print("LED on")
                    GPIO.output(18, GPIO.HIGH)
                elif "off" in command.lower():
                    print("LED off")
                    GPIO.output(18, GPIO.LOW)

            # Handle any errors
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that")
            except sr.RequestError as e:
                print("Error; {0}".format(e))

            # Wait for 1 second before listening again
            time.sleep(1)


if __name__ == '__main__':
    app = App()
    app.start


