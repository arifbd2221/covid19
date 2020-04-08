# This is the backend part of Covid-19 project.

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

 [goto localhost:8000/home/v2](http://127.0.0.1:8000/home/v2)
 
 ***
 ## Restapi's Uses
 ### To get world report on Covid-19
 Query: [goto localhost:8000/home/v2](http://127.0.0.1:8000/home/v2)
 
 Result:
 ```
 [
    {
        "country": "AFGHANISTAN",
        "states": 0,
        "confirmed": 367,
        "deaths": 8,
        "recovered": 18
    },
    .....,
    ......,
    ......
  ]
 ```
 
 ### To get a particular country report
 Query: [goto localhost:8000/{country name}/v2](http://127.0.0.1:8000/bangladesh/v2)
 
 Result:
 ```
    {
        "country": "Bangladesh",
        "states": 0,
        "confirmed": 123,
        "deaths": 12,
        "recovered": 33
    }
 ```
 
 ### To get daily reports on Deaths & Recoveries
 Query : [goto localhost:8000/today/v2](http://127.0.0.1:8000/today/v2)
 Result:
 ```
    {
        "country": "world",
        "states": 0,
        "confirmed": 0,
        "deaths": 70790,
        "recovered": 207398
    }
 ```
 ## Each api end points are updated after 5 minutes automatically.
