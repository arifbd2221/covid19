from rest_framework import views
from rest_framework.response import Response
import pandas as pd
from datetime import datetime,timedelta
from ..serializers import ReportSerializer
from rest_framework import status



def getDataReport(report_date,nation):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+report_date+'.csv'
    
    global data
    data = pd.read_csv(url,usecols = ['Country_Region','Confirmed', 'Deaths', 'Recovered'])
    countries = data['Country_Region']
    countries = countries.values.tolist()
    countries = set(countries)
    countries = list(countries)

    global modified_data_source
    modified_data_source = list()
    datalist = data.values.tolist()

    for c in countries:
        info_dict = dict()
        States=0
        Confirmed=0
        Deaths=0
        Recovered=0

        for item in datalist:
            if c == item[0]:
                States=States+1
                Confirmed=Confirmed+item[1]
                Deaths=Deaths+item[2]
                Recovered=Recovered+item[3]

        info_dict['country']= c.upper()
        info_dict['states'] = States
        info_dict['confirmed'] = Confirmed
        info_dict['deaths'] = Deaths
        info_dict['recovered'] = Recovered

        #print(info_dict['country'],nation)

        if info_dict['country'] == nation:
            return info_dict

        modified_data_source.append(info_dict)


def getWorldReport(data):
    total_confirmed = data['Confirmed']
    total_confirmed = total_confirmed.values.tolist()
    total_confirmed = sum(total_confirmed)

    total_deaths = data['Deaths']
    total_deaths = total_deaths.values.tolist()
    total_deaths = sum(total_deaths)
    
    total_recovered = data['Recovered']
    total_recovered = total_recovered.values.tolist()
    total_recovered = sum(total_recovered)


    info_dict = dict()
    info_dict['country']='world'
    info_dict['states'] = 0
    info_dict['confirmed'] = total_confirmed
    info_dict['deaths'] = total_deaths
    info_dict['recovered'] = total_recovered

    return info_dict


class ReportView(views.APIView):

    def get(self,request):
        try:
            prev_date = str((datetime.now() - timedelta(1)).strftime('%m-%d-%Y'))
            getDataReport(prev_date,"")
        except:
            date_2_days_ago = str((datetime.now() - timedelta(days=2)).strftime('%m-%d-%Y'))
            getDataReport(date_2_days_ago,"")

        results = ReportSerializer(modified_data_source,many=True).data

        return Response(results)


class WorldReport(views.APIView):
    def get(self,request):

        prev_date = str((datetime.now() - timedelta(1)).strftime('%m-%d-%Y'))
        date_2_days_ago = str((datetime.now() - timedelta(days=2)).strftime('%m-%d-%Y'))

        try:

            data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+prev_date+'.csv',
            usecols = ['Confirmed', 'Deaths', 'Recovered'])


            info_dict = getWorldReport(data)
            

            results = ReportSerializer([info_dict],many=True).data

            return Response(results)

        except:
            data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+date_2_days_ago+'.csv',
            usecols = ['Confirmed', 'Deaths', 'Recovered'])


            info_dict = getWorldReport(data)
            

            results = ReportSerializer([info_dict],many=True).data

            return Response(results)



class CountrysTotalReportView(views.APIView):

    def get(self,request):

        try:
            prev_date = str((datetime.now() - timedelta(1)).strftime('%m-%d-%Y'))
            getDataReport(prev_date,"")
        except:
            date_2_days_ago = str((datetime.now() - timedelta(days=2)).strftime('%m-%d-%Y'))
            getDataReport(date_2_days_ago,"")

        bangladesh = next(item for item in modified_data_source if item["country"] == "Bangladesh")
        results = ReportSerializer([bangladesh],many=True).data

        return Response(results)



"""

def getReportData(self):
        prev_date = str((datetime.now() - timedelta(1)).strftime('%m-%d-%Y'))
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-29-2020.csv'
        data = pd.read_csv(url,usecols = ['Country_Region','Confirmed', 'Deaths', 'Recovered'])

        countries = data['Country_Region']
        countries = countries.values.tolist()
        countries = set(countries)
        countries = list(countries)

        datalist = data.values.tolist()

        modified_data_source = list()

        for c in countries:
            info_dict = dict()
            States=0
            Confirmed=0
            Deaths=0
            Recovered=0

            for item in datalist:
                if c == item[0]:
                    States=States+1
                    Confirmed=Confirmed+item[1]
                    Deaths=Deaths+item[2]
                    Recovered=Recovered+item[3]

            info_dict['country']=c
            info_dict['states'] = States
            info_dict['confirmed'] = Confirmed
            info_dict['deaths'] = Deaths
            info_dict['recovered'] = Recovered

            modified_data_source.append(info_dict)

        return modified_data_source

"""




"""     del data['Province/State']
    infos = data.values.tolist()

    countryInfo = list()
    labels = ['Confirmed','','Deaths','Recovered','','', ' ']

    if request.method == 'POST':
        country = request.POST.get('country', None)
        
        if country:

            if len(country) == 2:
                country = country.upper()

            else:
                country = country.lower()
                country = country[0].upper() + country[1:]

            countries = data['Country/Region']
            countries=countries.tolist()

            for i,c in enumerate(countries):
                #print(len(c))
                if c == country:
                    info = ((data.loc[[i]]).values)[0]
                    listToStr = ' '.join(['' if j==1 or j==5 or j==6 else str(elem)+', '+labels[j] for j,elem in enumerate(info)])
                    countryInfo.append(listToStr)


    return render(request, 'app/home.html', {'infos': infos, 'countryInfo': countryInfo}) """



