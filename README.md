# clo835_project
CLO835 - Final Group Project


# Building Docker Images 

## MYSQL DB Image

```docker build -t my_db -f db/Dockerfile_mysql . ```



### Building application docker image 
```docker build -t my_app -f app/Dockerfile . ```

### Running mysql
```docker run -d -e MYSQL_ROOT_PASSWORD=pw  my_db```


### Setting env variables for app docker container
```
export DBHOST=172.17.0.2
export DBPORT=3306
```
```
export DBUSER=root
export DATABASE=employees
export DBPWD=pw
export APP_COLOR=blue
export s3link=https://gp-clo835.s3.amazonaws.com/test/1.png
```
### Run the application

```docker run -p 8080:8080  -e DBHOST=$DBHOST -e DBPORT=$DBPORT -e  DBUSER=$DBUSER -e DBPWD=$DBPWD -e s3link=$s3link  my_app```