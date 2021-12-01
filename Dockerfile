FROM python:3.8.0-slim
WORKDIR /usr/app
COPY ./ ./
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","chatbot.py"]
