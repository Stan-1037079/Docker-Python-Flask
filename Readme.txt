How to run the dockerfile 
In the terminal 
docker build -t <image_name> . (Builds a image for your container)
docker run -d -p 5000:5000 --<image_name> (When the image is build, start it)
docker ps (check if docker image is running)
docker ps -a (check all running containers)
docker logs <container_name> (check logs of container)
docker stop (stop the container from running)


