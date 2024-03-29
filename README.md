# clo835_project
CLO835 - Final Group Project


# Building Docker Images 

## MYSQL DB Image

```docker build -t my_db -f db/Dockerfile . ```



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
export S3_IMAGE_URI=https://gp-clo835.s3.amazonaws.com/test/1.png
export GROUP_NAME=name
export GROUP_SLOGAN=slogan
```
### Run the application

```docker run -p 8080:81  -e DBHOST=$DBHOST -e DBPORT=$DBPORT -e  DBUSER=$DBUSER -e DBPWD=$DBPWD -e S3_IMAGE_URI=$S3_IMAGE_URI -e GROUP_NAME=$GROUP_NAME -e GROUP_SLOGAN=$GROUP_SLOGAN my_app```