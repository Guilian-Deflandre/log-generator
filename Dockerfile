FROM python:3.8-slim
ADD src /src

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir Faker && \
    mkdir ./output && chmod ugo+rwx ./output

CMD ["python", "-m", "src.main"]