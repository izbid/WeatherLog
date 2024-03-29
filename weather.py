import logging
import logging.handlers
import os
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "weather_status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    api_TOKEN = os.environ["API_TOKEN"]
except KeyError:
    API_TOKEN = "Token not available!"
 

if __name__ == "__main__":
    logger.info(f"Token value: {API_TOKEN}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        weather = data["weather"]["description"]
        logger.info(f'Weather in Berlin: {weather},temp: {temperature}')