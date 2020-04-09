# This is the backend part of Covid-19 project.

## Data Sources
### [google spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQuDj0R6K85sdtI8I-Tc7RCx8CnIxKUQue0TCUdrFOKDw9G3JRtGhl64laDd3apApEvIJTdPFJ9fEUL/pubhtml?gid=0&single=true)
### [github](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/')

Used Tech Stack

## 1.Django
## 2.Beautifulsoap
## 3.Pandas

## Running on your Machine
First install requirements.txt file by the following command

```
pip install -r requirements.txt
```

 All right now you are ready to fly
 
 Finally run the below command to start the server

 `python manage.py runserver`

 [goto localhost:8000/api/v2/world/report/](http://127.0.0.1:8000/api/v2/world/report/)
 
 ***
 ## Restapi's Uses
 ### To get world report on Covid-19
 Query: [goto localhost:8000/api/v2/world/report/](http://127.0.0.1:8000/api/v2/world/report/)
 
 Result:
 ```
 [
    {
        "country": "Bangladesh",
        "states": 0,
        "confirmed": 330,
        "deaths": 21,
        "recovered": 33
    },
    .....,
    ......,
    ......
  ]
 ```
 
 ### To get a particular country report
 Query: [goto localhost:8000/api/v2/nation/{country}/](http://127.0.0.1:8000/api/v2/nation/{country}/)
 
 Result:
 ```
    {
        "country": "Bangladesh",
        "states": 0,
        "confirmed": 330,
        "deaths": 21,
        "recovered": 33
    }
 ```
 
 ### To get current day's report for a country
 Query : [goto localhost:8000/api/v2/daily/{country}/](http://127.0.0.1:8000/api/v2/daily/{country}/)
 Result:
 ```
    {
        "country": "Bangladesh",
        "states": 0,
        "confirmed": 112,
        "deaths": 1,
        "recovered": 0
    }
 ```
 
 
  ### To get total report on world wide
 Query : [goto localhost:8000/api/v2/total/report/](http://127.0.0.1:8000/api/v2/total/report/)
 Result:
 ```
    {
        "country": "world",
        "states": 0,
        "confirmed": 1576679,
        "deaths": 89678,
        "recovered": 272681
    }
 ```
 
 
 ## Each api end points are updated after 5 minutes automatically.
