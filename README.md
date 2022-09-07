# IDS706-Zilin

### How to run

Docker build to build the image
```
docker build -t <IMAGE> .  
```

Docker run to start the server
```
docker run -d --name <NAME> -p <DOCKER_PORT>:<HOST_PORT> <IMAGE>
```