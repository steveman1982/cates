FROM python:3.11-slim-buster

workdir cates

COPY main.py /cates/.
COPY requirements.txt /cates/.

ENV PYTHONUNBUFFERED=1

# TODO 
# frantic, yet unsuccesful attempt at trying to end up with headless opencv
# however I had to login to the container and remove both verions, and then
# reinstall headless again for it to work

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install gcc -y
RUN apt-get install python3-dev -y
RUN python3 -m ensurepip
RUN pip uninstall opencv-python -y
RUN pip install -r requirements.txt
RUN pip uninstall opencv-python -y
RUN pip uninstall opencv-python-headdless -y 
RUN pip install opencv-python-headless 

EXPOSE 5000

CMD ["python3", "main.py"]
