FROM python:3.10
WORKDIR /app
COPY . .
#COPY app/yocr-0.0.26.tar.gz .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install yocr-0.0.26.tar.gz
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
