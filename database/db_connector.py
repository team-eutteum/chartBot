from config.settings import get_connection
from datetime import datetime, timedelta


def get_chart_data(title: str, platform: str, type:str = 'realtime'):
    conn = get_connection()

    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)

    if platform == 'genie_chart':
        #2시 ~ 6시 차트운영 X -> 1시 데이터 제공
        start_time = now.replace(hour = 1, minute=0, second=0, microsecond=0)

    end_time = start_time + timedelta(hours=1)

    try:
        with conn.cursor() as cursor:
            sql = f"""
                SELECT title, `rank`, `change`
                FROM riizeStreaming.{platform}
                WHERE chart_type = %s
                AND title = %s
                AND crawled_at >= %s AND crawled_at < %s
            """

            cursor.execute(sql, (
                type,
                title,
                start_time,
                end_time
            ))

            results = cursor.fetchall()

    finally:
        conn.close()
        return results