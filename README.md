# chartBot

```
│  .env # 키 정보
│  main.py
│  README.md
│  requirements.txt
│
├─config # X api 연결 및 DB 세팅
│  │  settings.py 
│  │  __init__.py
│
├─database # DB 연결 및 순위 데이터 가져오는 코드
│  │  db_connector.py 
│  │  __init__.py
│
├─tweet
│  │  tweet_formatter.py # 음반사 별 순위 정보 텍스트 생성
│  │  tweet_sender.py # 트윗 전송 코드
│
└─utils
    │  logger.py # 로깅
    │  __init__.py

```

### 실행 방법
```commandline
python .\main.py '[곡 명]'

예시) python .\main.py 'Fly Up'
```