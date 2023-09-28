import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import wolframalpha
import pyautogui
import sys
import subprocess
from datetime import date
from plyer import notification
from bs4 import BeautifulSoup
import requests
import random
import time
import json
import psutil


print("                     Hi ! Im your virtual assistant AR-12 ^-^                     ")
print("---------------------------------------------------------------------------------")
name=input("What is your name? ")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
A=["hi","hello","hey","hai"]


def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("=============================")
        print('recognition is on:')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print(name, ':', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)
   
def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def make_request(url):
  response = requests.get(url)
  return response.text

def tell_day():
    localtime = time.asctime(time.localtime(time.time()))
    day = localtime[0:3]
    if day == "Sun":
        dd="it's sunday"
    if day == "Mon":
        dd=("it's monday")
    if day == "Tue":
        dd=("it's tuesday")
    if day == "Wed":
        dd=("it's wednesday")
    if day == "Thu":
        dd=("it's thursday")
    if day == "Fri":
        dd=("it's friday")
    if day == "Sat":
        dd=("it's saturday")
    print("AR-12: ",dd)
    speak_va(dd)
def tell_month():
    localtime = time.asctime(time.localtime(time.time()))
    m_onth = localtime[4:7]
    if m_onth == "Jan":
        m=("it's january")
    if m_onth == "Feb":
        m=("it's february")
    if m_onth == "Mar":
        m=("it's march")
    if m_onth == "Apr":
        m=("it's april")
    if m_onth == "May":
        m=("it's may")
    if m_onth == "Jun":
        m=("it's june")
    if m_onth == "Jul":
        m=("it's july")
    if m_onth == "Aug":
        m=("it's august")
    if m_onth == "Sep":
        m=("it's september")
    if m_onth == "Oct":
        m=("it's october")
    if m_onth == "Nov":
        m=("it's november")
    if m_onth == "Dec":
        m=("it's december")
    print("AR-12: ", m)
    speak_va(m)

def weather():
    city = input("Which city's weather would you like to know? ")
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")

def intro():
    print("Python programming language, developed by Guido Van Rossum in early 1990s,"
          "has become a very popular programming language among beginners as well as developers")
    speak_va("Python programming language, developed by Guido Van Rossum in early 1990s,"
          "has become a very popular programming language among beginners as well as developers")

def tokens():
    file1=open("tokens.txt","r")
    token2_read=file1.read()
    print(token2_read)
    speak_va(token2_read)

def barebones():
    file2=open("barebones.txt","r")
    bare1_read=file2.read()
    print(bare1_read)
    speak_va(bare1_read)

def mutable():
    file3=open("mutable.txt","r")
    mut1_read=file3.read()
    print(mut1_read)
    speak_va(mut1_read)

def lists():
    file4=open("lists1.txt","r")
    lis1_read=file4.read()
    print(lis1_read)
    speak_va(lis1_read)

def tup():
    file5=open("tuples1.txt","r")
    tup1_read=file5.read()
    print(tup1_read)
    speak_va(tup1_read)

def dic():
    file6=open("dictionary.txt","r")
    dic1_read=file6.read()
    print(dic1_read)
    speak_va(dic1_read)

def greet():
    C=["Hi,nice to meet you","Hello","Nice to meet you","Hey,nice to meet you","Good to meet you!"]
    b=random.choice(C)
    print("AR-12:", b)
    speak_va(b)

def activate_va():
    user_query = input_query()
    if 'time' in user_query:
        current_time = report_time()
        print(f"AR-12: the current time is {current_time}")
        speak_va(f"the current time is {current_time}")
    elif "date" in user_query:
        today=date.today()
        print("AR-12: Today's date is-->",today)
        speak_va(f"Today's date is {today}")
    elif 'day' in user_query and ('date' or 'month') not in user_query:
        tell_day()

    elif "month" in user_query:
        tell_month()
    elif user_query in A:
        greet()
    elif 'weather' in user_query:
        weather()

    elif 'open website' in user_query:
        speak_va(
            "AR-12: Please type the name of the website that you want to open (specify the full url) \n")
        website_name = input()
        print(website_name)
        webbrowser.get(
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(website_name)
        speak_va(f"{website_name} opened.")
    elif 'wikipedia' in user_query:
        speak_va("Searching on Wikipedia")
        user_query = user_query.replace('wikipedia', ' ')
        result = wikipedia.summary(user_query, sentences=4)
        print("AR-12:",result)
        speak_va(result)
    elif 'joke' in user_query:
        random_joke = pyjokes.get_joke()
        print("AR-12:",random_joke)
        speak_va(random_joke)
    elif 'screenshot' in user_query:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak_va('Screenshot taken.')
    elif 'learn python' in user_query:
        print("AR-12: Welcome! Choose the topic of your interest.")
        speak_va("Welcome ! Choose the topic of your interest.")
        ans='Y'
        while ans in 'Yy':
            print("-----------------------------------------------------")
            print("                    PYTHON TOPICS                    ")
            print("-----------------------------------------------------")
            print("                 1. Introduction                     ")
            print("                 2. Tokens In Python                 ")
            print("                 3. Barebones Of A Python Program    ")
            print("                 4. Mutable and Immutable Types      ")
            print("                 5. Lists                            ")
            print("                 6. Tuples                           ")
            print("                 7. Dictionaries                     ")
            ch=int(input("Enter your choice :"))
            if ch==1:
                intro()
            elif ch==2:
                tokens()
            elif ch==3:
                barebones()
            elif ch==4:
                mutable()
            elif ch==5:
                lists()
            elif ch==6:
                tup()
            elif ch==7:
                dic()
            else:
                print("Please enter the valid choice")
                sys.exit()
            speak_va("Do you want to continue?")
            ans=input("Do you want to continue?")
        speak_va("I hoped you learnt something about Python today!")
        print("I hoped you learnt something about Python today!")

    elif 'restaurant' in user_query:
        print("Welcome! Which cuisine are you going for?")
        speak_va("Welcome! Which cuisine are you going for?")
        ans='Y'
        while ans in 'Yy':
            print("-----------------------------------------------")
            print("                    CUISINE                    ")
            print("-----------------------------------------------")
            print("                   1. Indian                   ")
            print("                   2. Chinese                  ")
            print("                   3. Italian                  ")
            print("                   4. Thai                     ")

            print("           others: 5. Fast food                ")
            print("                   6. Street food              ")
            ch=int(input("Enter your choice : "))
            if ch==1:
                print("Here are some top indian cusine restaurants: ")
                speak_va("Here are some top indian cuine restaurants: ")
                webbrowser.open_new_tab("https://www.google.com/search?q=best+indian+cuisine+restaurants+in+bangalore&rlz=1C1CHBD_enAE914AE914&oq=top+indian+cuine+resta&aqs=chrome.3.69i57j0i13j0i22i30i457j0i22i30l7.18507j1j7&sourceid=chrome&ie=UTF-8")
            elif ch==2:
                print("Here are some top chinese cuisine restaurants: ")
                speak_va("Here are some top chinese cuisine restaurants: ")
                webbrowser.open_new_tab("https://www.google.com/search?q=top+chinese+restaurants+in+bangalore&rlz=1C1CHBD_enAE914AE914&oq=top+chinese+&aqs=chrome.1.0i433i512j0i512j69i57j0i512l7.4527j0j7&sourceid=chrome&ie=UTF-8")
            elif ch==3:
                print("Here are some top italian cuisine restaurants: ")
                speak_va("Here are some top italian cuisine restaurants: ")
                webbrowser.open_new_tab("https://www.google.com/search?q=top+italian+restaurants+in+bangalore&rlz=1C1CHBD_enAE914AE914&oq=top+ital&aqs=chrome.1.69i57j0i512l3j0i457i512j0i512l5.3919j0j7&sourceid=chrome&ie=UTF-8")
            elif ch==4:
                print("Here are some top thai cuisine restaurants: ")
                speak_va("Here are some top thai cuisine restaurants: ")
                webbrowser.open_new_tab("https://www.google.com/search?q=top+thai+restaurants+in+bangalore&rlz=1C1CHBD_enAE914AE914&oq=top+thai+restaurants+in+ba&aqs=chrome.3.0i512j69i57j0i512l2j0i22i30l6.13458j0j7&sourceid=chrome&ie=UTF-8")
            elif ch==5:
                print("Here are some top reviewed fast food restaurants: ")
                speak_va("Here are some top reviewed fast food restaurants: ")
                webbrowser.open_new_tab("https://www.zomato.com/bangalore/best-fast-food-restaurants")
            elif ch==6:
                print("Here are some top reviewed street food restaurants: ")
                speak_va("Here are some top reviewed street food restaurants: ")
                webbrowser.open_new_tab("https://traveltriangle.com/blog/street-food-in-bangalore/")
            else:
                print("Please enter a valid choice")
                sys.exit()
            speak_va("Do you want to continue?")
            ans=input("Do you want to continue?")
        speak_va("I hoped this was helpful!")
        print("I hope this was helpful")
               
    elif "online shopping" in user_query:
        print("Welcome! What are you looking for?")
        speak_va("Welcome! What are you looking for?")
        ans='Y'
        while ans in 'Yy':
            print("-------------------------------------------------------")
            print("                    ONLINE SHOPPING                    ")
            print("-------------------------------------------------------")
            print("                    1. Clothes                         ")
            print("                    2. Fruits and Vegetables           ")
            print("                    3. Electronic gagets               ")
            print("                    4. Food                            ")
            print("                    5. Furniture                       ")
            print("                    6. All in one                      ")
            ch=int(input("Enter your choice: "))
            if ch==1:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. Urbanic ")
                print(" 2. Myntra  ")
                print(" 3. Ajio    ")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("https://www.urbanic.com/")
                elif ch1==2:
                    webbrowser.open_new_tab("https://www.myntra.com/")
                elif ch1==3:
                    webbrowser.open_new_tab("https://www.ajio.com/")
            elif ch==2:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. Big Basket ")
                print(" 2. Spar       ")
                print(" 3. Living Food ")
                ch2=int(input("Enter your choice: "))
                if ch2==1:
                    webbrowser.open_new_tab("https://www.bigbasket.com/cl/fruits-vegetables/")
                elif ch2==2:
                    webbrowser.open_new_tab("https://www.sparindia.com/categories/root-fruits-and-vegetables/cid-CI59634913.aspx")
                elif ch2==3:
                    webbrowser.open_new_tab("https://livingfood.co/")
            elif ch==3:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. Apple ")
                print(" 2. Samsung ")
                print(" 3. Lenovo ")
                print(" 4. LG ")
                print(" 5. All in one (Reliance Digital) ")
                ch3=int(input("Enter your choice: "))
                if ch3==1:
                    webbrowser.open_new_tab("https://www.apple.com/in/")
                elif ch3==2:
                    webbrowser.open_new_tab("https://www.samsung.com/in/")
                elif ch3==3:
                    webbrowser.open_new_tab("https://www.lenovo.com/in/en/")
                elif ch3==4:
                    webbrowser.open_new_tab("https://www.lg.com/in")
                elif ch3==5:
                    webbrowser.open_new_tab("https://www.reliancedigital.in/")
            elif ch==4:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. Swiggy ")
                print(" 2. Zomato ")
                print(" 3. Uber Eats ")
                ch4=int(input("Enter your choice: "))
                if ch4==1:
                    webbrowser.open_new_tab("https://www.swiggy.com/")
                elif ch4==2:
                    webbrowser.open_new_tab("https://www.zomato.com/")
                elif ch4==3:
                    webbrowser.open_new_tab("https://www.ubereats.com/")
            elif ch==5:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. IKEA ")
                print(" 2. Urban Ladder ")
                ch5=int(input("Enter your choice: "))
                if ch5==1:
                    webbrowser.open_new_tab("https://www.ikea.com/in/en/")
                elif ch5==2:
                    webbrowser.open_new_tab("https://www.urbanladder.com/")
            elif ch==6:
                print("Which website do you want to shop from?")
                speak_va("Which website do you want to shop from?")
                print(" 1. Amazon ")
                print(" 2. Flipkart ")
                ch6=int(input("Enter your choice: "))
                if ch6==1:
                    webbrowser.open_new_tab("https://www.amazon.in/")
                elif ch6==2:
                    webbrowser.open_new_tab("https://www.flipkart.com/")
            else:
                print("Please enter a valid choice")
                sys.exit()
            speak_va("Do you want to continue?")
            ans=input("Do you want to continue?")
        speak_va("I hoped this was helpful!")
        print("I hope this was helpful")
    elif ("college" or "university") in user_query:
        print("Which field do you want college recommendations for? ")
        speak_va("Which field do you want college recommendations for? ")
        ans='Y'
        while ans in 'Yy':
            print("--------------------------------------------------------")
            print('                    AREA OF INTEREST                    ')
            print("--------------------------------------------------------")
            print("                    1. Engineering")
            print("                    2. Medical")
            print("                    3. Law")
            print("                    4. Business")
            print("                    5. Architecture")
            ch=int(input("Enter your choice: "))
            if ch==1:
                print("Do you want to proceed with 1. Government or 2. Private ?")
                speak_va("Do you want to proceed with 1. Government or 2. Private ?")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("https://home.iitd.ac.in/")
                if ch1==2:
                    webbrowser.open_new_tab("https://www.bits-pilani.ac.in/")
            elif ch==2:
                print("Do you want to proceed with 1. Government or 2. Private ?")
                speak_va("Do you want to proceed with 1. Government or 2. Private ?")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("https://www.aiims.edu/en.html")
                if ch1==2:
                    webbrowser.open_new_tab("https://manipal.edu/kmc-manipal.html")
            elif ch==3:
                print("Do you want to proceed with 1. Government or 2. Private ?")
                speak_va("Do you want to proceed with 1. Government or 2. Private ?")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("https://www.nls.ac.in/")
                if ch1==2:
                    webbrowser.open_new_tab("https://jgu.edu.in/jgls/")
            elif ch==4:
                print("Do you want to proceed with 1. Government or 2. Private ?")
                speak_va("Do you want to proceed with 1. Government or 2. Private ?")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("https://www.iima.ac.in/")
                if ch1==2:
                    webbrowser.open_new_tab("https://www.nmims.edu/")
            elif ch==5:
                print("Do you want to proceed with 1. Government or 2. Private ?")
                speak_va("Do you want to proceed with 1. Government or 2. Private ?")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    webbrowser.open_new_tab("http://spa.ac.in/Home.aspx?ReturnUrl=%2f")
                if ch1==2:
                    webbrowser.open_new_tab("https://manipal.edu/foa.html")
            else:
                print("Please enter a valid choice")
                sys.exit()
            speak_va("Do you want to continue?")
            ans=input("Do you want to continue?")
        speak_va("I hoped this was helpful!")
        print("I hope this was helpful")
    elif "where is" in user_query:
        user_query = user_query.split(" ")
        speak_va("Hold on, I will show you where " + user_query[2] + " is.")
        print("Hold on, I will show you where " + user_query[2] + " is.")
        webbrowser.open_new_tab("https://www.google.com/maps/place/"+str(user_query[2]))
               
           
           
    elif 'search' in user_query:
        print("AR-12: What do you want me to search for (please type) ?")
        speak_va("What do you want me to search for (please type) ? ")
        search_term = input()
        search_url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get(
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
        speak_va(f"here are the results for the search term: {search_term}")
    elif 'news'in user_query:
        print("AR-12: Here's the latest news")
        speak_va("Here's the latest news")
        webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
        time.sleep(5)
    elif 'covid' in user_query:
      html_data = make_request('https://www.worldometers.info/coronavirus/')
      # print(html_data)
      soup = BeautifulSoup(html_data, 'html.parser')
      total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
      total_cases = total_global_row.find_all('td')[2].get_text()
      new_cases = total_global_row.find_all('td')[3].get_text()
      total_recovered = total_global_row.find_all('td')[6].get_text()
      print('AR-12: total cases : ', total_cases)
      print('       new cases', new_cases[1:])
      print('       total recovered', total_recovered)
      notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
      notification.notify(
        title="COVID-19 Statistics",
        message=notification_message,
        timeout=5
      )
      speak_va("here are the stats for COVID-19")
   
    elif 'who are you' in user_query or 'what can you do' in user_query:
        f=open("who_are_you.txt","r")
        read_1=f.read()
        print("AR-12:",read_1)
        speak_va(read_1)
    elif "how are you" in user_query:
        print("AR-12: I am good, how about you?")
        speak_va("I am good, how about you?")
        question=input_query()
        if ("good" in question or "fine" in question or "okay" in question) and "not" not in question:
            print("AR-12: :)")
            speak_va( "^-^" )
        elif "not good" in question or "not fine" in question or "not okay" in question:
            print("AR-12: I hope it gets better.")
            speak_va("I hope it gets better")

    elif "who made you" in user_query or "who created you" in user_query or "who discovered you" in user_query:
            print("AR-12: I was built by Rithika and Avantika")
            speak_va("I was built by Ritheeka and Avantika")
   
    elif 'ask' in user_query:
            print("I can answer computational and geographical questions. What question do you want to ask")
            speak_va(' I can answer computational and geographical questions . You can ask me one question now')
            question=input_query()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak_va(answer)
            print("AR-12: ",answer)
    elif 'bye' in user_query:
        print('Thank you for using AR-12')
        speak_va('Thank you for using AR-12')
        sys.exit()
    elif 'log off' in user_query or 'sign out' in user_query:
        speak_va("ok, your pc will log off in 10 secs make sure you exit from all applications")
        subprocess.call(["shutdown","/l"])
        time.sleep(3)
       
while True:
    activate_va()
