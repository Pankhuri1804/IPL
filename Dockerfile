FROM python:3.8
RUN mkdir -p /IPL
COPY . /IPL
WORKDIR /IPL
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
