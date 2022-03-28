FROM python:3.6
WORKDIR /test
COPY library-script .
RUN pip install -r requirements.txt
CMD python main.py
