FROM python:3.8-slim
ADD src /logger
WORKDIR /logger
RUN mkdir output
CMD ["python", "./main.py"]