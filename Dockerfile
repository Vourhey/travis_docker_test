FROM alpine:latest

RUN apk add bash python3 \
   && mkdir /work
COPY *.py /work/
WORKDIR /work
RUN chmod +x test_script.py
CMD "/work/test_script.py"

