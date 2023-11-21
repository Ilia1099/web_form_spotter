ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR opt/src/

COPY ./requirements.txt /opt/src/requirements.txt

RUN apt-get update
RUN apt-get install nano -y
RUN pip3 install --no-cache-dir --upgrade -r /opt/src/requirements.txt

COPY ./app /opt/src/app/
COPY ./wtf_tmpls.json .


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


