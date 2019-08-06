FROM python:3.7
WORKDIR /work

CMD apt update && \
    apt install -y zip && \
    mkdir -p python/bin && \
    pip install -t ./python requests lxml selenium && \
    curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip && \
    unzip headless-chromium.zip -d python/bin/ && \
    rm headless-chromium.zip && \
    curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip && \
    unzip chromedriver.zip -d python/bin/ && \
    rm chromedriver.zip && \
    zip -r ./zipdir/layer.zip python
