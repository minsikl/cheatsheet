# Docker examples

This page contains examples of docker commands. 

## Lanuch a new ubuntu docker container. 

Launch a new docker container with a ubuntu image.

```
docker run -i -t ubuntu /bin/bash
```

Launch a new docker container with _--rm_ option. The container will be deleted if a process of the container dies.
```
docker run -i -t --rm ubuntu /bin/bash
```

## Build nodejs and redis components.

Start a redis docker container.
```
docker run -d -P --name redis redis
```

Check the port of the redis container.
```
docker port redis
```

Create a  Dockerfile:
```
FROM readytalk/nodejs
RUN npm install redis
ADD app.js /
WORKDIR /
ENTRYPOINT ["/nodejs/bin/node","app"]
```

Create a nodejs application:
```
var redis = require('redis');
var client = redis.createClient(process.env.REDIS_PORT_6379_TCP_PORT, process.env.REDIS_PORT_6379_TCP_ADDR);

client.on('connect', function() {
    console.log('connected');
});

client.set('language', 'golang', function(err, reply) {
    console.log(reply);
});

client.get('language', function(err, reply) {
    console.log(reply);
});
```

Build a nodejs docker image:
```
docker build -t minsikl/nodejs_example .
```

Lanunch a nodejs container
```
docker run --link redis minsikl/nodejs_example
```

## Start a redis process with a restart option. 
```
docker run -d -P --restart unless-stopped --name redis redis
```

## Use data volume
```
docker create -v /usr/local/var/lib/couchdb --name db-data alpine /bin/true
docker run -d -p 5984:5984 -v /usr/local/var/lib/couchdb --name db1 --volumes-from db-data couchdb
```
# Docker-compose examples
Create a `docker-compose.yml` file
```
version: "3"
services:
  redis1:
   image: redis
```

Lanuch, stop, delete a docker container.
```
docker-compose up -d
docker-compose ps
docker-compose stop
docker-compose rm
```

# Splunk log configuration
Configure a splunk container.
```
docker run -d -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_USER=root" -p "8000:8000" -p "8088:8088" splunk/splunk
docker run --name redis --log-driver=splunk --log-opt splunk-token=[TOKEN] --log-opt splunk-url=http://127.0.0.1:8088 -d redis

```

docker-compose.yml for splunk
```
version: "3"
services:
  splunk1:
   image: splunk/splunk
   ports:
    - "8000:8000"
    - "8088:8088"
   environment:
    - SPLUNK_START_ARGS=--accept-license
    - SPLUNK_USER=root
```
