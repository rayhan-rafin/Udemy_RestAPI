FROM python:3.14
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000", "--debug"]

#docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api