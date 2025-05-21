import sys

from datetime import datetime
from database.db_connector import get_chart_data
from tweet.tweet_formatter import format_tweet
from tweet.tweet_sender import send_tweet
from utils.logger import setup_logger

def run_bot(title: str):
    melon_data = get_chart_data(title, 'melon_chart','top100')
    genie_data = get_chart_data(title, 'genie_chart')
    bugs_data = get_chart_data(title, 'bugs_chart')
    flo_data = get_chart_data(title, 'flo_chart')

    now = datetime.now().strftime('%m/%d %H:%M')
    header = "🧡" + title + " 차트 순위 | " + now + "🧡" +"\n"
    hashTag = title.replace(" ", "")

    # 전송할 문구 formatter
    melon_text = format_tweet(melon_data, '멜론 TOP100')
    genie_text = format_tweet(genie_data, '지니 TOP200')
    bugs_text = format_tweet(bugs_data, '벅스 실시간')
    flo_text = format_tweet(flo_data, '플로 실시간')

    footer = "\n" + '#RIIZE #라이즈 #' + hashTag + ' #' + hashTag +'_RIIZE #ODYSSEY'

    tweet_text = header + melon_text + genie_text + bugs_text + flo_text + footer

    # 트윗 전송 함수
    send_tweet(tweet_text)

if __name__ == "__main__":
    logger = setup_logger("tweet")

    if len(sys.argv) < 2:
        logger.info("title을 인자로 입력해주세요.")
        sys.exit(1)

    title = sys.argv[1]
    run_bot(title)
