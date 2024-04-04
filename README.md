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



### K8s

`eksctl create cluster -f eks_config.yaml`

`eksctl delete cluster --name clo835 --region us-east-1` 


Commands:

- create a ns

`k create ns final`





## Database:

- Secrets for mysql username and pass
- Imagepull secret to pull ECR image
- PersistentVolumeClaim based on gp2 default StorageClass: 
o Size: 2Gi
o AccessMode: ReadWriteOnce

- Deployment of MySQL DB with 1 replica and volume based on PVC
- Service that exposes MySQL DB to the Flask application.

Commands:

`kubectl create secret generic db-sec --from-file=./secrets/ -n final`
`kubectl create secret generic db-ecr --from-file=.dockerconfigjson=/home/ec2-user/.docker/config.json --type=kubernetes.io/dockerconfigjson -n final`

`kubectl apply -f storageclass.yaml`
`kubectl apply -f pvc.yaml -n final`
`kubectl apply -f db-deployment.yaml -n final`
`kubectl apply -f db-service.yaml -n final`

## App

Configmap for bg image URL
Secrets for AWS credentails to allow s3 private bucket access
Imagepull secret to pull ECR image
Deployment of Flask application with 1 replica
Service that exposes the Flask application to the Internet users and has a stable endpoint




Create serviceaccount named “clo835”
K8s role (Role or ClusterRole, whichever is appropriate) “CLO835” with permissions to create and read namespaces. Create a binding (RoleBinding or ClusterRoleBinding, whichever appropriate) that binds the “CLO835” role to the clo835 serviceaccount.