## Weather Status Logger: 

The weather.py script is designed to retrieve weather information for a specific location by making an API call to a weather service. 
This application is unique as it's set up to run as a cron job using GitHub Actions, allowing for regular, automated updates.

### Basic features
* Automated Weather Logging: Utilizes GitHub Actions to schedule and run the script at specified intervals.
* Weather Data Retrieval: Makes API calls to a weather service to get real-time weather data.
* Logging: Records the weather data into a weather_status.log file for historical tracking and analysis.

### GitHub Actions and Free Tier Usage
This application leverages the GitHub Actions feature, making the most out of the 2000 free minutes available per month on GitHub's free tier. 
This approach is not only cost-effective but also demonstrates a practical application of GitHub Actions for automation projects.

## Basic Setup
1.  GitHub Actions Configuration:
*  The cron job is configured in the .github/workflows/weather_cronjobs.yml file.
*  Modify the schedule in the YAML file to set the desired frequency for the script execution.
2.  API Token Configuration:
*  Ensure that the API_TOKEN environment variable is set in your GitHub repository settings for secure API access.
3.  Logging Configuration:
*  The script writes output to weather_status.log.
*  Log file management (e.g., rotation, backup) is handled within the script.

