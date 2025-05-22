import sys

from datetime import datetime, timedelta
from database.db_connector import get_chart_data
from tweet.tweet_formatter import format_tweet
from tweet.tweet_sender import send_tweet
from utils.logger import setup_logger

def run_bot(title: str):
    melon_data = get_chart_data(title, 'melon_chart','top100')
    genie_data = get_chart_data(title, 'genie_chart')
    bugs_data = get_chart_data(title, 'bugs_chart')
    flo_data = get_chart_data(title, 'flo_chart') #이전 시간 차트

    day_text = ''

    # 13시: 일간차트 추가
    if datetime.now().hour == 13:
        melon_day_data = get_chart_data(title, 'melon_chart', 'genre100')
        melon_day_text = format_tweet(melon_day_data, '멜론 일간')

        day_text = melon_day_text + '\n'

    now = datetime.now().strftime('%m/%d %H시')
    header = "🪽" + title + " 차트 순위 | " + now +"\n"
    hashTag = title.replace(" ", "")

    #flo 용 시간
    hour_ago = datetime.now() - timedelta(hours=1)
    hour_ago = hour_ago.strftime('%m/%d %H시')

    # 전송할 문구 formatter
    melon_text = format_tweet(melon_data, '멜론 TOP100')
    genie_text = format_tweet(genie_data, '지니 TOP200')
    bugs_text = format_tweet(bugs_data, '벅스 실시간')
    flo_text = '\n\n' + hour_ago + format_tweet(flo_data, '플로 실시간')

    footer = "\n\n" + '🔥스밍 계속 체크하기🔥' + "\n\n" + '#RIIZE #라이즈 #' + hashTag + ' #' + hashTag +'_RIIZE #ODYSSEY'

    tweet_text = header + day_text + melon_text + genie_text + bugs_text + flo_text  + footer

    # 트윗 전송 함수
    send_tweet(tweet_text)

if __name__ == "__main__":
    logger = setup_logger("tweet")

    if len(sys.argv) < 2:
        logger.info("title을 인자로 입력해주세요.")
        sys.exit(1)

    title = sys.argv[1]
    run_bot(title)
