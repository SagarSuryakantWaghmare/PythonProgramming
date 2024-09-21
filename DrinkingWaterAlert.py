import time
import pyttsx3

def drink_water_alert():
    engine = pyttsx3.init()
    engine.say("It's time to drink water!")
    engine.runAndWait()

def main():
    water_interval = 60 * 60  # Time interval in seconds (1 hour in this case)

    try:
        while True:
            time.sleep(water_interval)  # Sleep for the specified interval
            drink_water_alert()

    except KeyboardInterrupt:
        print("Drinking water alert application terminated.")

if __name__ == "__main__":
    main()
