Codigo inspirado en 
https://runnable.com/docker/python/dockerize-your-flask-application y en https://github.com/leah/hello-flask-heroku/

Pero actualizado a Python3 y Ubuntu 20.04

```
docker build -t flask-tutorial:latest .
```
```
docker run -d -p 5000:5000 flask-tutorial
```
