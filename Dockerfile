FROM python:3.8

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && rm -f ./requirements.txt

COPY . ./

EXPOSE 8501
CMD ["streamlit", "run", "src/streamlit_example/app.py"]