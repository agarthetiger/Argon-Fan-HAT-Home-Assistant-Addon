ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on

RUN \
  apk add --no-cache \
    python3 \
    openjpeg \
    tiff \
    openblas-dev \
    py3-pip

FROM python:3
RUN \
  pip install --upgrade pip && \
  pip install --no-cache-dir pillow && \
  pip install --no-cache-dir numpy && \
  pip3 install --no-cache-dir gpiod && \
  pip3 install --no-cache-dir smbus

COPY bin/main.py /bin/main.py
COPY lib/waveshare_pwm_fan_hat/ /lib/waveshare_pwm_fan_hat/

CMD [ "python", "./bin/main.py" ]
