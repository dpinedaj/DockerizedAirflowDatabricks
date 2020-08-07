#image build on centos
FROM centos:7

# Environment variables to use as root (not recommended always), and airflow home
ENV AIRFLOW_HOME=/usr/local/airflow
ENV C_FORCE_ROOT="true"

# Update system and install necessary packages
RUN yum update -y \
    && yum install -y https://repo.ius.io/ius-release-el7.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && yum install -y which gcc \ 
    && yum install -y openldap-devel \
    && yum install -y wget \
    && yum install -y libaio \
    && yum autoremove -y

# Create pip simbolic link (because i like it)
RUN ln -s /usr/bin/pip3.6 /bin/pip
# Install necessary python packages
RUN pip install psycopg2-binary \
    && pip install "apache-airflow[databricks, celery, password, redis, flower, crypto]" \
    && pip install flask-bcrypt

# Make necessary folders for volumes
RUN mkdir -p /usr/local/airflow/dags \
    && mkdir -p /usr/local/airflow/logs \
    && mkdir -p /usr/local/airflow/libraries \
    && mkdir -p /usr/local/airflow/modules



# Copy necesary files to initialize and configs
COPY ./src/airflow/airflow.cfg /usr/local/airflow/airflow.cfg
COPY ./src/airflow/init.sh /usr/local/airflow/init.sh
COPY ./src/airflow/userPrompt.py /usr/local/airflow/userPrompt.py
COPY ./src/airflow/packages.pth /usr/lib/python3.6/site-packages

WORKDIR /usr/local/airflow/

