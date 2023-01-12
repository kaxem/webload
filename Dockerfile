FROM python:3
RUN pip install bs4 \
    && pip install requests \
    && pip install html5lib
COPY . /app
WORKDIR  /app
CMD python3 main.py
