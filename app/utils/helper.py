from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
from ..views import github_report_views


def getDailyReportForCountry(nation):
    result = dict()
    c_dict = dict() 
    try:
        prev_date = str((datetime.now() - timedelta(1)).strftime('%m-%d-%Y'))
        c_dict = github_report_views.getDataReport(prev_date,nation)
        c_list = getReport(nation)

        #print(c_dict)
        print(c_list)

        result['country'] = 'daily'
        result['states'] = 0
        result['deaths'] = abs(int((c_list[0])['deaths']) - (c_dict['deaths']))
        result['confirmed'] = abs(int((c_list[0])['confirmed']) - (c_dict['confirmed']))
        result['recovered'] = abs(int((c_list[0])['recovered']) - (c_dict['recovered']))

        return [result]

    except:
        date_2_days_ago = str((datetime.now() - timedelta(days=2)).strftime('%m-%d-%Y'))
        c_dict = github_report_views.getDataReport(date_2_days_ago,nation)
        c_list = getReport(nation)

        result['country'] = 'daily'
        result['states'] = 0
        result['deaths'] = abs(int((c_list[0])['deaths']) - (c_dict['deaths']))
        result['confirmed'] = abs(int((c_list[0])['confirmed']) - (c_dict['confirmed']))
        result['recovered'] = abs(int((c_list[0])['recovered']) - (c_dict['recovered']))

        return [result]

    

def getTotalConfirmedCase():
    return getReport("t")

def getReport(nation):
    #translator = Translator()
    url1="https://docs.google.com/spreadsheets/d/e/2PACX-1vQuDj0R6K85sdtI8I-Tc7RCx8CnIxKUQue0TCUdrFOKDw9G3JRtGhl64laDd3apApEvIJTdPFJ9fEUL/pubhtml?gid=0&single=true"

    t_confirm = 0


    main_report = requests.get(url1)
    soup = BeautifulSoup(main_report.content, 'html.parser')

    result = soup.find('tbody')

    rows = result.find_all('tr')

    all_reports=list()

    try:
        #print("top",nation)
        for i,data in enumerate(rows):
            if i==0:
                continue
            #print("inside loop")

            country = ((data.contents)[2].contents)[0]


            info_dict = dict()
            info_dict['country'] = country #(translator.translate(country, dest="bn")).text
            info_dict['states'] = 0
            info_dict['confirmed'] = ((data.contents)[3].contents)[0]
            info_dict['deaths'] = ((data.contents)[4].contents)[0]
            info_dict['recovered'] = ((data.contents)[5].contents)[0]

            t_confirm = t_confirm + int(info_dict['confirmed'])

            if country == nation:
                return [info_dict]

            #print(nation)
            all_reports.append(info_dict)
    except:
        pass
    
    if nation == "t":
        return t_confirm
    else:
        return sorted(all_reports, key=lambda k: int(k['deaths']),reverse=True)
    

def getTodaysReport():
    url2="https://docs.google.com/spreadsheets/d/e/2PACX-1vQuDj0R6K85sdtI8I-Tc7RCx8CnIxKUQue0TCUdrFOKDw9G3JRtGhl64laDd3apApEvIJTdPFJ9fEUL/pubhtml?gid=636567047&single=true"
    daily_report = requests.get(url2)
    
    html = BeautifulSoup(daily_report.content, 'html.parser')
    today = str((datetime.now()).strftime('%m/%d'))

    daily_result = html.find('tbody')

    daily_rows = daily_result.find_all('tr')

    for i,d in enumerate(daily_rows):
        if i==0 or i==1:
            continue
        date = ((d.contents)[1].contents)[0].split(' ')
        
        if date[0] == today and len(date)==2:
            report = dict()
            report['country'] = "world"
            report['states'] = 0
            report['confirmed'] = getTotalConfirmedCase()
            report['deaths']=((d.contents)[5].contents)[0]
            report['recovered']=((d.contents)[8].contents)[0]

            return [report]


