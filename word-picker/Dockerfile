FROM python:3.12
WORKDIR /code
RUN pip install flask
ENV FLASK_APP=/code/word_picker.py
ADD options.txt /code/
COPY word_picker.py /code/word_picker.py
CMD ["flask", "run", "-h", "0.0.0.0"]
