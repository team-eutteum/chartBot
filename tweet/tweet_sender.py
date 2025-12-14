import tweepy
import time

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

    # 헤더 확인용 로그 기록 추가
    except tweepy.TooManyRequests as e:
        response = getattr(e, "response", None)

        if response and response.headers:
            headers = response.headers

            limit = headers.get("x-rate-limit-limit")
            remaining = headers.get("x-rate-limit-remaining")
            reset = headers.get("x-rate-limit-reset")

            now = int(time.time())

            if reset:
                reset = int(reset)
                wait_seconds = reset - now
            else:
                wait_seconds = None

            logger.error(
                "[RATE LIMIT]\n"
                f"limit={limit}, remaining={remaining}, reset={reset}, "
                f"wait_seconds={wait_seconds}"
            )
        else:
            logger.error("[RATE LIMIT] 헤더 정보 없음")

    except Exception as e:
        logger.error(f"트윗 전송 실패: {e}")