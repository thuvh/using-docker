FROM debian:wheezy

MAINTAINER Hoai-Thu Vuong <thuvh87@gmail.com>
RUN apt-get update && apt-get install -y cowsay fortune

COPY entrypoint.sh /bin

ENTRYPOINT ["/bin/entrypoint.sh"]

