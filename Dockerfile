# pull official base image
FROM python:3.9.13-alpine

# install dependencies
RUN apk --update --upgrade add build-base alpine-sdk gcc g++ musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev


# copy the requirements file into the image
COPY ./requirements.txt /usr/src/app/requirements.txt

# switch working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt


# Add app
COPY . /app

EXPOSE 5000
# Run flask development server
CMD python main.py run -h 0.0.0.0