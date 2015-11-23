FROM ipython/scipyserver

MAINTAINER Patrick White <whitep@vcu.edu>

RUN cp /usr/local/bin/pip2 /usr/local/bin/pip

ENV PATH /notebooks/miniconda2/bin:$PATH

VOLUME /notebooks
WORKDIR /notebooks
