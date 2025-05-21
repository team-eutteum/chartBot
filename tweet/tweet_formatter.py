from utils.logger import setup_logger

def format_tweet(data: list[tuple], header) -> str:
    logger = setup_logger("tweet")

    if not data:
        logger.info(header +  ' 차트 데이터 없음 - 차트 미진입')
        return "\n" + f"header: ⚠️차트 미진입⚠️"

    lines = []
    for item in data:
        rank = item[1]
        change = int(item[2])

        if change > 0:
            change_symbol = "🔺" + str(abs(change))
        elif change < 0:
            change_symbol = "🔻" + str(abs(change))
        else:
            change_symbol = "="

        lines.append(f"{header}: {rank}위({change_symbol})")

    return "\n" + "\n".join(lines)
