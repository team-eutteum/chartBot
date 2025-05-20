import tweepy

from config.settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from utils.logger import setup_logger

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def send_tweet(text: str):
    logger = setup_logger("tweet")

    try:
        client.create_tweet(text=text)
        logger.info("트윗 전송 성공")

    except Exception as e:
        logger.error(f"트윗 전송 실패: {e}")