import os
import webbrowser as wb
import random
import pyttsx3 
import speech_recognition as sr
import datetime as dt
import AppOpener as ao
import pyautogui as ptg
def fin(p,f):
    l=[]
    dir=os.listdir(p)
    for i in dir:
        if f.lower() in i.lower():
            a=os.path.join(p,i)
            l.append(a)
        try: 
            p2=os.path.join(p,i) 
            d2=os.listdir(p2)
            for i in d2:
                if f.lower() in i.lower():
                    a = os.path.join(p2, i)
                    l.append(a)
                try:
                    fin(os.path.join(p2,i),f)
                except PermissionError as e:
                    pass
                except NotADirectoryError as e:
                    pass
        except PermissionError as e:
            pass
        except NotADirectoryError as e:
            pass
    return l

def fout(url):    
    if url=="youtube":
        url="http://www.youtube.com"
    elif url=="bing":
        url="http://www.bing.com"
    elif url=="google":
        url="http://www.google.com"
    elif url=="python":
        url="https://www.python.org"
    wb.open_new(url)
    
def spk(vc):
    e=pyttsx3.init()
    a=e.getProperty("voices")
    e.setProperty("voice", a[1].id)# setting voice
    e.setProperty("rate",125)# setting rate
    e.setProperty("volume",1.0)# setting volume
    e.say(vc)# speaking
    e.runAndWait()

def wish():
    t=str(dt.datetime.now())
    a=t.split(" ")
    h=int((a[1].split(":"))[0])
    if h>0 and h<12:
        return("Good morning")
    elif h>12 and h<18:
        return("Good afternoon")
    elif h>18:
        return("Good evening")
    
def open(src):
    ao.open(src)

def close(src):
    ao.close(src)

def lstn():
    r= sr.Recognizer()
    with sr.Microphone() as src:
        print("listening...")
        r.pause_threshold=0.5
        r.energy_threshold=1500
        aud=r.listen(src)
    try:
        print(f"recognizing...")
        q=r.recognize_google(aud,language="en-in")
        print(q)
        return q
    except Exception:
        print("voivce not recognized")
        return "none"

#start of body

st=lstn()    
if "hello" in st.lower():
    u="Dhruv"
    spk(f"{wish()} {u}, How can I help you.")
    s=" "
    while True:
        st=lstn()
        print(st)
        l=st.split(" ")
        if "repeat" in l:
            spk(s)
        elif "open" in l:
            n=l.index("open")
            open(l[n+1])
        elif "close" in l:
            n=l.index("open")
            close(l[n+1])
        elif "find" in l:
            n=l.index("find")
            file=l[n+1]
            n=l.index("in")
            path=l[n+1]
            if len(str(path)) <= 1:
                fl=fin(f"{path}://",file)   
            else:
                fl=fin(f"{path}//",file)
            for i in fl:
                print(i)
                spk(i)
        elif "search" in l:
            n=l.index("search")
            fout(l[n+1])
        elif "tell" in l:
            n=l.index("tell")
            a=l[n+1:len(l)]
            t=str(dt.datetime.now()).split(" ")
            print(t)
            if "time" in a:
                lt=str(t[1]).split(":")
                s=f"right now it is {lt[0]} hours, {lt[1]} minute,{lt[2]} seconds"
            elif "date" in a:
                mon=["january","february","march","april","may","june","july","august","october","november","december"]
                lt=t[0].split("-")
                m=int(lt[1])
                s=f"today is {lt[2]} of {mon[m]} of {lt[0]}"
            elif "day" in a:
                wd=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
                w=dt.datetime.isoweekday(dt.datetime.now())
                s=f"today is {wd[w]}"
            else:
                s="what"
        elif "play" in l:
            n=l.index("play")
            a=l[n+1:len(l)]
            msc=fin("D://",".mp3")
            vdo=fin("D://",".mp4")
            if "music" in a:
                rfl=len(msc)
                print(rfl)
                r=random.randint(0,rfl)
                os.startfile(msc[r])
            elif "video" in a:
                rfl=len(msc)
                print(rfl)
                r=random.randint(0,rfl)
                os.startfile(msc[r])
            else:                
                for ad in msc:
                    for i in a:
                        if i.lower() in str(ad).lower():
                            os.startfile(ad)
                            break 
                for ad in vdo:
                    for i in a:   
                        if i.lower() in str(ad).lower():
                            os.startfile(ad)
                            break

        else:
            s=" "
        spk(s)
        spk("anything else")
