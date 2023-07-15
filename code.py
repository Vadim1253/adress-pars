import os  
from time import sleep
from turtle import st
import googletrans
from googletrans import Translator
from selenium import webdriver
import pyperclip
from geopandas.tools import geocode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import eel
import re
from selenium.webdriver.firefox.service import Service
eel.init("web")
@eel.expose
def cfc(z,sta):
    city=z.split("\n")
    file=open(r'adress.txt',encoding='utf-8')
    gorf=file.readlines()
    gor=[None]*2
    adr=[None]*2
    i1=i2=0
    i=0
    res=""
    print("Вывод метобом "+sta+".\nЛоо и Обь проверить")
    print(type(sta))
    sta=int(sta)
    for g in gorf:
        if " " in g:
            if i1==0 or i1==1:
                adr[i1]=g
                stt1=adr[i1]
                stt1=stt1[:-1]
                adr[i1]=stt1
                i1=i1+1
            else:
                st1=g
                st1=st1[:-1]
                adr.append(st1)
        else:
            if i2==0 or i2==1:
                gor[i2]=g
                stt2=gor[i2]
                stt2=stt2[:-1]
                gor[i2]=stt2
                i2=i2+1
            else:
                st2=g
                st2=st2[:-1]
                gor.append(st2)
                
    for q in city:
        st3=q
        st3=st3[:-1]
        # st3=st3+","
        # print(st3)
        q=st3
        par=[None]*2
        i1=0
        for a in adr:
            # adr=re.split(adr)
            # if (" "+q+"") in a:
            # if q in (" "+a):
            
            if sta == 1:
                if q in a:
                    if i1==0 or i1==1:
                        par[i1]=a
                        i1=i1+1
                    else:
                        par.append(a)
            elif sta == 2:
                aa=a[:-1]
                if aa.endswith(q):
                    if i1==0 or i1==1:
                        par[i1]=a
                        i1=i1+1
                    else:
                        par.append(a)
        i=i+1
        ss=random.choice(par)
        if ss==None:
            for a in adr:
                if sta == 1:
                    if q in a:
                        if i1==0 or i1==1:
                            par[i1]=a
                            i1=i1+1
                        else:
                            par.append(a)
                elif sta == 2:
                    aa=a[:-1]
                    if aa.endswith(q):
                        if i1==0 or i1==1:
                            par[i1]=a
                            i1=i1+1
                        else:
                            par.append(a)
            i=i+1
            ss=random.choice(par)
            if ss==None:
                for a in adr:
                    if sta == 1:
                        if q in a:
                            if i1==0 or i1==1:
                                par[i1]=a
                                i1=i1+1
                            else:
                                par.append(a)
                    elif sta == 2:
                        aa=a[:-1]
                        if aa.endswith(q):
                            if i1==0 or i1==1:
                                par[i1]=a
                                i1=i1+1
                            else:
                                par.append(a)
                i=i+1
                ss=random.choice(par)
                if ss==None:
                    for a in adr:
                        if sta == 1:
                            if q in a:
                                if i1==0 or i1==1:
                                    par[i1]=a
                                    i1=i1+1
                                else:
                                    par.append(a)
                        elif sta == 2:
                            aa=a[:-1]
                            if aa.endswith(q):
                                if i1==0 or i1==1:
                                    par[i1]=a
                                    i1=i1+1
                                else:
                                    par.append(a)
                    i=i+1
                    ss=random.choice(par)
                    if ss==None:
                        ss="None"
        
        res=res+ss+"\n"
    # eel.sh(res,i)
    eel.sh(res)
    # print(ss)
eel.show()

@eel.expose
def pars(ci,serc):
    print(serc)
    serc=serc.replace(' ','%20')
    print(serc)
    ci=ci.split("\n")
    for g in ci:
        os.environ['MOZ_HEADLESS']='1'
        service = Service(executable_path="/geckodriver")
        brow=webdriver.Firefox(service=service)
        sleep(1)
        brow.get(url=f"https://yandex.ru/maps/194/saratov/search/{serc}%20в%20{g}/")
        sleep(1)
        et=brow.find_elements(By.CLASS_NAME, "search-business-snippet-view__address")
        for i in et:
            print(i.text)
            eel.sh1(i.text)
        # sleep(1)
        brow.quit()
        # sleep(1)
eel.show()

@eel.expose
def ind(ad):
    ii=0
    # file=open(r'C:\Users\kryue\Desktop\PyScript\indexi\adress.txt',encoding='utf-8')
    #filea=open(r'\Users\Vadim\Desktop\2.txt','w',encoding='utf-8')
    # gorf=file.readlines()
    gorf=ad.split("\n")
    os.environ['MOZ_HEADLESS']='1'
    service = Service(executable_path="/geckodriver")
    brow=webdriver.Firefox(service=service)
    i=0
    brow.get(url="https://openaddress.ru/search?search-fias-address=%D1%83%D0%BB.+%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%91%D0%B2%D0%B0%2C+1%D0%90%2C+%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA&search-type=fias")
    for g in gorf:
        
        if i==100 or i==200 or i==300 or i==400 or i==500 or i==600 or i==700 or i==800 or i==900 or i==1000:
            brow.close()
            brow=webdriver.Firefox()
            brow.get(url="https://openaddress.ru/search?search-fias-address=%D1%83%D0%BB.+%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%91%D0%B2%D0%B0%2C+1%D0%90%2C+%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA&search-type=fias")
        zz=brow.find_element(By.XPATH, "//*[@id=\"search-fias-address\"]")
        zz.click()
        zz.clear()
        zz.send_keys(g)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div/div[2]/button").click()
        sleep(2)
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/table/tbody/tr[1]/td[1]")
        q=zz.text
        print(q)
        i=i+1
        ii=ii+1
        eel.sh2(q)
        
eel.show()
@eel.expose
def tra(ci):
    ii=0
    # file=open(r'C:\Users\kryue\Desktop\PyScript\indexi\adress.txt',encoding='utf-8')
    #filea=open(r'\Users\Vadim\Desktop\2.txt','w',encoding='utf-8')
    # gorf=file.readlines()
    gorf=ci.split("\n")
    os.environ['MOZ_HEADLESS']='1'
    service = Service(executable_path="/geckodriver")
    brow=webdriver.Firefox(service=service)
    brow.get(url="http://translit-online.ru/")
    for g in gorf:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        zz.click()
        zz.clear()
        zz.send_keys(g)
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
        qq=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]")
        qq1=qq.text
        qq2=qq1.lower()
        qq2=qq2.replace('\'','')
        print(qq2)
        eel.sh3(qq2)
eel.show()

@eel.expose
def sprr(ci,sta):
    gorf=ci.split("\n")
    sta=int(sta)
    os.environ['MOZ_HEADLESS']='1'
    service = Service(executable_path="/geckodriver")
    brow=webdriver.Firefox(service=service)
    for g in gorf:
        brow.get(url=f"https://morpher.ru/Demo.aspx?s={g}")
        if sta == 1:
            # xp="/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[10]/td[3]/span"
            zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[10]/td[3]/span")
        elif sta == 2:
            # xp="/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[6]/td[3]/span"
            zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[6]/td[3]/span")
        elif sta == 3:
            # xp="/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[9]/td[3]/span"
            zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/div/div/table/tbody/tr[9]/td[3]/span")
        # zz=brow.find_element(By.XPATH, xp)
        
        print(zz.text)
        eel.sh4(zz.text)
@eel.expose
def ko(ci,sta):
    sta=int(sta)
    gorf=ci.split("\n")
    if sta == 1:
        service = Service(executable_path="/geckodriver")
        brow=webdriver.Firefox(service=service)
        for g in gorf:
            brow.get(url="https://snipp.ru/tools/address-coord")
            zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/ymaps/ymaps[5]/ymaps/ymaps[1]/ymaps/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps")
            zz.click()
            zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/ymaps/ymaps[5]/ymaps/ymaps[1]/ymaps/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[2]/input")
            zz.click()
            zz.clear()
            zz.send_keys(g)
            brow.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/ymaps/ymaps[5]/ymaps/ymaps[1]/ymaps/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps[2]/ymaps/ymaps[2]/ymaps").click()
            
            brow.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div/div/span").click()
            #brow.find_element(By.XPATH, "//*[@id=\"ypoint-copy\"]").click()
            zz1=pyperclip.paste()
            print(zz1)
            eel.sh5(zz1)
    elif sta == 2:
        for g in gorf:
            i=0
            i1=0
            loc = g
            loc=loc[:-1]
            translator = Translator()
            # loc = translator.translate(f"{loc}", src='ru', dest='en')
            # translation=translator.translate("Привет", src="ru", dest="ar")
            # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            # print(loc.text)
            location = geocode(loc, provider="nominatim" , user_agent = 'my_request')
            i1=i1+1
            if "None" in str(location):
                loc=loc.rsplit(',',1)[0]
                location = geocode(loc, provider="nominatim" , user_agent = 'my_request')
                if "None" in str(location):
                    loc=loc.rsplit(',',1)[0]
                    location = geocode(loc, provider="nominatim" , user_agent = 'my_request')
                    if "None" in str(location):
                        ss="None"
                        ss=str(ss)
                        print(ss)
                        eel.sh5(ss)
                        continue
            point = location.geometry.iloc[i]
            xx=format(point.x)
            yy=format(point.y)
            print(xx+", "+yy)
            ss=str(xx+", "+yy)
            eel.sh5(ss)
    #filea.write(f"{zz1}\n")
        #filea.write(f"{zz1.text}\n")
eel.show()
eel.start("index.html", size=(700,1100))
