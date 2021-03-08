# Just Averaged - 30 Day Averaged Bitlink Metics
Just Averaged is an API that pulls Bitlink country click data and returns each countries 30 day average clicks.

Just Average combines your bitlink and the 30 day average per country into a single JSON snippet.

```
{
  "avgs": [
    {
      "30_day_avg": 23.733333333333334, 
      "country": "US"
    }, 
    {
      "30_day_avg": 0.2, 
      "country": "ZA"
    }, 
    {
      "30_day_avg": 0.16666666666666666, 
      "country": "SE"
    }, 
    {
      "30_day_avg": 0.06666666666666667, 
      "country": "SG"
    }, 
    {
      "30_day_avg": 0.03333333333333333, 
      "country": "UA"
    }
  ], 
  "bitlink": "bit.ly/3kHENK4"
}
```
## Quick Start
1. Install Docker
2. Clone git repo with ***git clone git@github.com:ispeakcomputer/bitly_api.git***
3. Run ***cd bitly_api***
4. Add your Bitly API Token to BITLYTOKEN=
5. run ***docker build -t just_average -f Dockerfile .*** Do not forget the dot at the end
6. run ***docker run -it -p 88:5000 just_average***
7. Skip to and follow the README section called ***Query The API*** below


## Linux Installation 
1. Clone git repo with ***git clone git@github.com:ispeakcomputer/bitly_api.git***
2. Run ***cd bitly_api***
3. If you use an environment then ***python3 -m venv venv***
3. Run ***source venv/bin/activate*** to activate your environment
4. Run  ***pip install -r /path/to/requirements.txt*** to install modules for app
5. Add your Bitly Token to BITLYTOKEN= in the start_here.sh file
6. Run ***chmod +x start_here.sh*** to allow executing the script
7. Run ./start_here.sh to run

## Query The API

These instructions are for using with Docker instructions above.
Use with port 5000 if running on local system

1. First you need to get your JWT code from the /login endpoint

```
curl -X POST -H "Content-Type: application/json"  
           -d '{"username":"test","password":"test"}' 
	   http://127.0.0.1:88/login
```
2. Then use the returned token to retrieve your data from the / endpoint
```
curl -H 'Authorization: Bearer <TOKEN HERE>' -X GET http://0.0.0.0:88
```

## Development Setup
When populating data to be used for this API you will need to create click data for bitlinks on your Bitly account. You can use a VPN to add clicks from any country and the bash snippet below to 'automate' clicks.

Bitly doesn't regsister clicks via the curl's user agent and curl must follow redirects as this is how Bitly captures metrics in the first place, so use the following curl command to populate data for your accounts bitlinks
```
while sleep 5; do curl -A  "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" -L https://bit.ly/9000420; done
```
