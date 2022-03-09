FROM python:3.8-slim
ADD src /logger
WORKDIR /logger
 
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir Faker && \
    mkdir output

CMD ["python", "./main.py"]