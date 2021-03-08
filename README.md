# Just Averaged - 30 Day Averaged Bitlink Metics
------------------------

Just Averaged is an API that pulls Bitlink country click data and returns each countries 30 day averaged clicks.

## Linux Installation 
-------------------------
1. Clone git repo with ***git clone git@github.com:ispeakcomputer/bitly_api.git***
2. Run ***cd bitly_api***
3. If you use an environment then ***python3 -m venv venv***
3. Run ***source venv/bin/activate*** to activate your environment
4. Run  ***pip install -r /path/to/requirements.txt*** to install modules for app

## Launch Docker Container
--------------------------
1. Clone git repo with ***git clone git@github.com:ispeakcomputer/bitly_api.git***
2. Run ***cd bitly_api***
3. docker build -t just_average -f Dockerfile .
4. docker run -it -p 88:5000 just_average

## Play With The API
---------------------
1. First you need to get your JWT code
```
curl -X POST -H "Content-Type: application/json"  
           -d '{"username":"test","password":"test"}' 
	   http://127.0.0.1:88/login
```
2. Then use it to retrieve your data
```
curl -H 'Authorization: Bearer <TOKEN HERE>' -X GET http://0.0.0.0:88
```


