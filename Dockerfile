FROM python:3.6

RUN mkdir /RevdolAdmin

WORKDIR /RevdolAdmin

ADD . /RevdolAdmin

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/ selenium

EXPOSE 8000

ENTRYPOINT ["python","/RevdolAdmin/manage.py","runserver","0.0.0.0:8000"]