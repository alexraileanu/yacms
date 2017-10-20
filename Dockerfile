FROM ubuntu:17.04
RUN apt update -y

ENV FLASK_APP index.py
ENV LC_ALL 'C.UTF-8'
ENV LANG 'C.UTF-8'

RUN apt install -y  python3-pip \
                    python3-dev \
                    build-essential \
                    vim \
                    libmariadbclient-dev

WORKDIR /var/www/yacms
COPY requirements.txt .

RUN pip3 install flask_user
RUN pip3 install -r requirements.txt
COPY . .

COPY ./config/config.example.cfg ./config/config.cfg
CMD ["python3", "index.py"]
