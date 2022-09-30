FROM mysql

ENV MYSQL_DATABASE docker_project
ENV MYSQL_ROOT_PASSWORD <insert_pass>
ENV MYSQL_USER joe
ENV MYSQL_PASSWORD <insert_pass>

# Define mountable directories.
VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Define working directory.
WORKDIR /data

COPY ./initialize.sql /docker-entrypoint-initdb.d/

# Expose ports.
EXPOSE 3306
