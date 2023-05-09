# Pull any base image that includes python3
FROM python:3.10

# install the toolbox runner tools
RUN pip install json2args

# install era5cli
RUN pip install era5cli

# install additional dependencies
RUN pip install python-dotenv

# create the tool input structure
RUN mkdir /in
COPY ./in /in
RUN mkdir /out
RUN mkdir /src
COPY ./src /src

WORKDIR /src

# create folder to store api credentials
RUN mkdir -p /root/.config/era5cli

CMD ["python", "run.py"]
