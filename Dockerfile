FROM python:3.9

WORKDIR /siteabouttravellingflask

COPY frontend/templates/404.html ./templates/404.html
COPY frontend/templates/china.html ./templates/china.html
COPY frontend/templates/index.html ./templates/index.html
COPY frontend/templates/countries.html ./templates/countries.html
COPY frontend/templates/feedback.html ./templates/feedback.html

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

CMD ["python", "/siteabouttravellingflask/run.py"]
