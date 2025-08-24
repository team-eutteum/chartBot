from utils.logger import setup_logger

def format_tweet(data: list[tuple], header) -> str:
    logger = setup_logger("tweet")

    if not data:
        logger.info(header +  ' 차트 데이터 없음 - 차트 미진입')
        return "\n" + header + ": ⚠️차트 미진입⚠️"

    lines = []
    for item in data:
        rank = item[1]
        change_str = item[2] #'new' 또는 숫자 문자열
        # change = int(item[2])

        #신규 진입
        if change_str.lower() == "new":
            change_symbol = "🆕"

        else:
            try:
                change = int(change_str)

                if change > 0:
                    change_symbol = "🔺" + str(abs(change))
                elif change < 0:
                    change_symbol = "▼" + str(abs(change))
                else:
                    change_symbol = "="

            except ValueError:
                change_symbol = "" #숫자 변환 실패 시 기본값

        lines.append(f"{header}: {rank}위 ({change_symbol})")

    return "\n" + "\n".join(lines)
