FROM ipython/ipython:latest

MAINTAINER Patrick White <whitep@vcu.edu>

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

ENV LANG C.UTF-8

#ENTRYPOINT [ "/usr/bin/tini", "--" ]

ADD notebook.sh /
CMD ["/notebook.sh"]
