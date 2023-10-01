FROM python:3.9

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt 

COPY . /

EXPOSE 8000

CMD [ "uvicorn", "gene_info.main:app", "--host", "0.0.0.0", "--port", "8000"]