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
export DBHOST=172.XX.0.2
export DBPORT=3306
```
```
export DBUSER=root
export DATABASE=employees
export DBPWD=pw
export S3_IMAGE_URI=s3://clo835testbucketerccardiel/unpath/bg_1.jpg
export GROUP_NAME=name
export GROUP_SLOGAN=slogan
export AWS_ACCESS_KEY_ID=XXX
export AWS_SECRET_ACCESS_KEY=XXX
export AWS_SESSION_TOKEN=XXX
```
### Run the application

```docker run -p 8080:81  -e DBHOST=$DBHOST -e DBPORT=$DBPORT -e  DBUSER=$DBUSER -e DBPWD=$DBPWD -e S3_IMAGE_URI=$S3_IMAGE_URI -e GROUP_NAME=$GROUP_NAME -e GROUP_SLOGAN=$GROUP_SLOGAN -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN my_app```