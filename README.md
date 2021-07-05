# Intro

La idea es aprender a programar cosas simples en Flask, poderlas dockerizar o publicar en Heroku. 

- Manejo de argumentos en la URL
- Implementar templates
- Manejo de bases de datos

# Referencias

Codigo inspirado en 
- https://runnable.com/docker/python/dockerize-your-flask-application
- https://github.com/leah/hello-flask-heroku/
- https://www.udemy.com/course/learn-complete-devops-with-python-docker-kubernetes-git

Pero actualizado a Python3 y Ubuntu 20.04

# Docker

```
docker build -t flask-tutorial:latest .
```
```
docker run -d -p 5000:5000 flask-tutorial
```

# Heroku

```
git clone https://github.com/cayu/aprendiendo-flask.git
cd aprendiendo-flask/
heroku create
git push heroku main
heroku logs --tail
```
