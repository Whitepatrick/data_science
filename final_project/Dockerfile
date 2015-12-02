FROM  python:2.7
MAINTAINER Patrick White <whitep@vcu.edu>

RUN printf "deb http://ftp.us.debian.org/debian/ jessie main contrib non-free\ndeb-src http://ftp.us.debian.org/debian/ jessie main contrib non-free" > /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install --no-install-recommends -yq build-essential \
curl \
python \
python-dev \
make \
gcc \
gfortran \
tree \
vim \
libopenblas-dev \
liblapack-dev \
python-dev \
&& apt-get clean

RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install --upgrade pip
RUN pip install --upgrade numpy
RUN pip install --upgrade scipy
RUN pip install --upgrade scikit-learn
RUN pip install --upgrade pandas
RUN pip install --upgrade matplotlib
RUN pip install --upgrade seaborn
RUN pip install --upgrade ipython[notebook]
RUN pip install --upgrade nose

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ADD reqs.txt /tmp
COPY .customrc /root/.bashrc
RUN pip install -r /tmp/reqs.txt
RUN source /root/.bashrc
RUN rm /tmp/reqs.txt

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

ADD notebook.sh /

CMD ["/notebook.sh"]
