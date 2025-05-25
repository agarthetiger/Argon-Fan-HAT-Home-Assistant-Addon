ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on

RUN \
  apk add --no-cache \
    python3 \
    py3-pip

FROM python:3-slim
RUN \
  pip install --upgrade pip && \
  pip3 install --no-cache-dir gpiod && \
  pip3 install --no-cache-dir smbus

COPY bin/main.py /bin/main.py

CMD [ "python", "./bin/main.py" ]
