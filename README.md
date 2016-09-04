# using docker

## Using Docker in Development

### Say "Hello World!"

```docker run -d -p 5000:5000 -v "$(pwd)"/app:/app identidock```

-v bind mount absoulte path to absolute path in container,

```docker stop $(docker ps -lq)
docker rm $(docker ps -lq)```

stop and remove container

create user and group of uwsgi as usual 
expose port
run as user 

expose and run as user
-e in docker run to push environment variable to container

docker-compose

### Creating a Simple Web App

simple source code in indentidock2
link to dnmonster image
working with other name

