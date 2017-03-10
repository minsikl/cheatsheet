# Docker example

Launch a new docker container with a ubuntu image.

```
docker run -i -t ubuntu /bin/bash
```

Launch a new docker container with _--rm_ option. The container will be deleted if a process of the container dies.
```
docker run -i -t --rm ubuntu /bin/bash
```

