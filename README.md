# using docker

## Using Docker in Development

### Say "Hello World!"

```docker run -d -p 5000:5000 -v "$(pwd)"/app:/app identidock```

-v bind mount absoulte path to absolute path in container,

```docker stop $(docker ps -lq)
docker rm $(docker ps -lq)```

stop and remove container



 
