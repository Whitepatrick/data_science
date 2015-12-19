FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
		python-dev \
		wget \
		curl \
		git \
		vim \
		libfreetype6 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 1.9

RUN pip install --upgrade pip
RUN pip install mysqlclient psycopg2 django=="$DJANGO_VERSION"

RUN pip install --upgrade numpy scipy pandas scikit-learn matplotlib
RUN pip install --upgrade patsy seaborn ipython[notebook] statsmodels
RUN pip install --upgrade nose imdbpy wget mysqldbda ipywidgets
