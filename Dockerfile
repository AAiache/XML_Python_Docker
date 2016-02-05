FROM python:latest

RUN pip install lxml

ADD validateXML.py /

RUN echo '#!/bin/sh' > check.sh
RUN echo 'python validateXML.py $1.xml $1.xsd' >> check.sh
RUN chmod +x check.sh

