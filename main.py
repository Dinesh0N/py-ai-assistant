import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
from googlesearch import search
from ecapture import ecapture as ec
import wolframalpha
from decouple import config
import smtplib
from twilio.rest import Client

from settings import (
    AI_NAME,
    MY_PHONE_NUMBER,
    ACCOUNT_SID,
    AUTH_TOKEN,
    GMAIL_USER,
    GMAIL_PASSWORD,
    WOLFRAM_APP_ID
)

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')      # 0 for male, 1 for female

# speak text -> speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    speak_current_hour()

def speak_current_hour():
    # greet the user
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def take_command():
    # understand and accept human language
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I'm sorry, can you please say that again")
            return "None"
        return statement.lower()

def wiki_help(input):
    speak("Searching Wikipedia ...")
    input = input.replace("wikipedia","")
    results = wikipedia.summary(input, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)


def open_webpage(input):
    webbrowser.open_new_tab(f"https://www.{input}.com")
    speak(f"{input} is open now")
    time.sleep(5)

def search_with_google(input):
    result_list = []
    for result in search(input,num=1):
        result_list.append(result)
    print(result_list)
    speak(f"Searching for input")
    webbrowser.open_new_tab(result_list[0])
    speak(f"{input} is open now")
    time.sleep(5)

def check_current_time(input):
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Current time is {str_time}")

def search_local_news():
    webbrowser.open_new_tab(f'https://www.timesofmalta.com/articles/latest')
    speak('Loading Times of Malta headlines')
    time.sleep(6)

def take_photo():
    ec.capture(0,"robo camera","img.jpg")

def wolfram_ask(input):
    app_id = WOLFRAM_APP_ID
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    res = client.query(input)
    answer = next(res.results).text
    speak(answer)
    print(answer)

def send_email():

    sent_from = gmail_user
    to_email = input('Enter to email here: ')
    to = [to_email]
    subject = input('Enter Email Subject here: ')
    body = input('Enter body of email here: ')
    email_text = """
    From:{}
    To:{}
    Subject:{}

    {}
    """.format(sent_from, ", ".join(to), subject, body)
    print(email_text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')


def send_whatsapp():
    from_whatsapp_number = "whatsapp:+14155238886"
    # from_whatsapp_number = "whatsapp:" + input("Whatsapp message from: ")
    # to_whatsapp_number = "whatsapp:" + input("Whatsapp message to: ")
    # body = input("Whatsapp message content: ")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # client.messages.create({
    # body: body,
    # from_: from_whatsapp_number,
    # to: to_whatsapp_number
    # })

    client.messages.create(
    from_='whatsapp:+35679081894',
    body='This is a test from jeremy',
    to='whatsapp:+35679072600'
    )


def inbuilt_commands(statement):

    # feature 1: fetch data from wikipedia
    if "wikipedia" in statement:
        wiki_help(statement)

    # feature 2: access web browser
    elif "open youtube" in statement:
        webpage = "youtube"
        open_webpage(webpage)

    elif "open google" in statement:
        webpage = "google"
        open_webpage(webpage)

    elif "open gmail" in statement:
        webpage = "gmail"
        open_webpage(webpage)

    elif "open website" in statement:
        webpage = take_command()
        open_webpage(webpage)

    elif "search with google" in statement:
        search_subject = take_command()
        search_with_google(search_subject)

    elif "local news" in statement or "times of malta" in statement:
        search_local_news()

    elif "take photo" in statement:
        take_photo()

    elif "ask wolfram" in statement:
        question = take_command()
        wolfram_ask(question)

    elif "send email" in statement:
        send_email()

    elif "send whatsapp" in statement:
        send_whatsapp()





    # feature 3: Speak current time
    elif "current time" in statement:
        check_current_time(statement)

    # feature 4:


def main():
    greet_me()

    while True:
        speak("How can I help you?")
        statement = take_command()
        if statement == 0:
            continue

        inbuilt_commands(statement)


        if f"{AI_NAME} shut down" in statement or f"stop" in statement:
            speak("Ok, shutting down now, good bye")
            print("Ok, shutting down now, good bye")
            break



if __name__ == "__main__":
    main()
