ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip
RUN pip3 install --upgrade pip3 && \
  pip3 install --no-cache-dir gpiod && \
  pip3 install --no-cache-dir smbus

COPY bin/main.py /bin/main.py

CMD [ "python", "./bin/main.py" ]
