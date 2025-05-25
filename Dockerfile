ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    openjpeg \
    py3-pip

FROM python:3
RUN \
  pip install --upgrade pip && \
  pip3 install --no-cache-dir gpiod && \
  pip3 install --no-cache-dir smbus

COPY bin/main.py /bin/main.py
COPY lib/argon_fan_hat/ /lib/argon_fan_hat/

CMD [ "python", "./bin/main.py" ]
