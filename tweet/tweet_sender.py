import tweepy
import time
from datetime import datetime

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
        logger.error({e})

        response = e.response
        if response is not None:
            headers = response.headers

            limit = headers.get("x-rate-limit-limit")
            remaining = headers.get("x-rate-limit-remaining")
            reset = headers.get("x-rate-limit-reset")

            # reset을 사람이 보기 좋은 형태로 변환
            if reset:
                reset_epoch = int(reset)
                now_epoch = int(time.time())
                wait_seconds = max(reset_epoch - now_epoch, 0)

                reset_time = datetime.fromtimestamp(
                    reset_epoch
                ).strftime("%Y-%m-%d %H:%M:%S")

                logger.error(
                    f"rate-limit-limit={limit}, "
                    f"remaining={remaining}, "
                    f"reset={reset} ({reset_time}, {wait_seconds}초 후)"
                )
            else:
                logger.error(
                    f"rate-limit-limit={limit}, remaining={remaining}, reset=None"
                )
        else:
            logger.error("429 발생했으나 response 객체 없음")

    except Exception as e:
        logger.error(f"트윗 전송 실패: {e}")