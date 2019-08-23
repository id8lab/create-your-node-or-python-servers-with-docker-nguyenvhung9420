FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY src/ /app                                                                           

EXPOSE 80

ENTRYPOINT  ["python3"]

CMD ["main.py"]