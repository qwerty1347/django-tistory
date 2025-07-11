# python 베이스 이미지 사용
FROM python:3.11

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# MySQL client 개발 패키지, 빌드 필수 도구 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 설치
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# entrypoint.sh 복사 및 권한 부여
COPY .docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]