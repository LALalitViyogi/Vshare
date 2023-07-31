# Using Python:3.10 Base Image
FROM python:3.10


# Making Working Directory
WORKDIR /VShare

# Transferring files to working directory
COPY . .

# Installing Required Dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]


