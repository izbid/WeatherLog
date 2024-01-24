## Schedule scripts as cron jobs using GitHub Actions: 


This ```weather.py``` script makes an api call to a weather service and obtains the weather of particular location.

It is scheduled as a cronjob to run at specific times using GitHub Actions and It logs the returned response into a 

```weather_status log file```. Github provides 2000mins/month of github actions under its free tier, this can be used in 

several automation projects like this one.

### Basic setup

*  Configure cron job in GitHub Action as in  ``` .github/workflows/weather_cronjobs.yml ```
