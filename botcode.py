import requests
import datetime

import time

import math




#==========================================vaccine_notifier Function starts==============================
def vaccine_notifier():

    theday = datetime.date.today()
    start = theday - datetime.timedelta(days=0)
    dates = [start + datetime.timedelta(days=d) for d in range(3)]

    #=====================================================================

    listOfAllCentresFor45=[]
    listOfAllCentresFor18=[]

    for d in dates:
        d1=str(d.strftime("%d-%m-%Y"))
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(686575,d1)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
        x = requests.get(url)
        data = x.json()
        print(data)
        cnt1=1
        cnt2=1
        centre_detail_1 = ""
        centre_detail_2 = ""

        centre_detail_1 = centre_detail_1 + "Date: "+ d1 + "\n\n" 
        centre_detail_2 = centre_detail_2 + "Date: "+ d1 + "\n\n"

        for d in data["sessions"]:
            if d["min_age_limit"] == 45:
                centre_detail_1 =centre_detail_1 + "Centre {0}: ".format(cnt1) + "\nCentre Adrress: " + d['name'] + ", " + d["address"] + "\nVaccine: " + d['vaccine'] + "\nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + '\n'
                listOfAllCentresFor45.append(centre_detail_1)
                centre_detail_1=''
                cnt1=cnt1+1

            elif d["min_age_limit"] == 18:
                centre_detail_2 =centre_detail_2 + "Centre {0}: ".format(cnt2) + "\nCentre Adrress: " + d['name'] + ", " + d["address"] + "\nVaccine: " + d['vaccine'] + "\nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + '\n'
                listOfAllCentresFor18.append(centre_detail_2)
                centre_detail_2=''
                cnt2=cnt2+1

    #============================Sending TELEGRAM MESSAGE=======================================

    messageFor45 = ""

    if len(listOfAllCentresFor45) >0:
        messageFor45 = messageFor45 + "*Available  vaccination centres for 45 plus:*\n\n"
        for mess in  listOfAllCentresFor45:
            messageFor45 = messageFor45 + mess
            messageFor45 = messageFor45 + "\n"

    else:
        messageFor45 = messageFor45 + "*No slot available for 45 and above age*"


    base_url = 'https://api.telegram.org/bot1750625715:AAHfM1JQlxJGvYMFBpZtd9iL9kklmC7l0A8/sendMessage?chat_id=-421663974&text={0}'.format(messageFor45)
    print("Response:",requests.get(base_url))
    print("Message Sent for 45+!")

    #----------------------------------------------------------------------------
    messageFor18 = ""

    if len(listOfAllCentresFor18) >0:
        messageFor18 = messageFor18 + "*Available  vaccination centres for 18 and above age:*\n\n"
        for mess in  listOfAllCentresFor18:
            messageFor18 = messageFor18 + mess
            messageFor18 = messageFor18 + "\n"

    else:
        messageFor18 = messageFor18 + "*No slot available for 18 and above age*"

    base_url = 'https://api.telegram.org/bot1750625715:AAHfM1JQlxJGvYMFBpZtd9iL9kklmC7l0A8/sendMessage?chat_id=-421663974&text={0}'.format(messageFor18)
    print("Response:",requests.get(base_url))
    print("Message Sent for 18+!")

#==========================================vaccine_notifier Function ends==============================


#--------------------------scheduling notification-------------------------
if __name__ == "__main__":
    print("executing")
    vaccine_notifier()
