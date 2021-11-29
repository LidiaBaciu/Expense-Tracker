FROM python:3.8-alpine
RUN mkdir /expense_tracker
ADD . /expense_tracker
WORKDIR /expense_tracker
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]