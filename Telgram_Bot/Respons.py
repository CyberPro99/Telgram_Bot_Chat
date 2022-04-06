from datetime import datetime

url = input("Enter Youtub Link :")

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey! How's it going?"
    
    if user_message in ("who are you","who"):
        return "Hi I'am Mr.Bot Here To Help You 😎"

    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%H:%S")
        return str(date_time)
    if user_message in ("1,1),one"):
        print("You Chose To Download Vdio As Mp4 !!")
        print(url)
        
        return "I Dont understad You!!"
    