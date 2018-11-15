#
# Deploy the zip file to an existing AWS Elastic Beanstalk app/environment
#

# Update the variables to match your environment
echo Deploy to AWS
BUCKET_NAME=elasticbeanstalk-us-east-1-134953076769
AWS_S3_BUCKET=s3://$BUCKET_NAME
AWS_ELASTIC_BEANSTALK_ENVIRONMENT=PythonTest2-env
AWS_ELASTIC_BEANSTALK_APPLICATION=python-test2
APP_FILE=app.zip
APP_VERSION=1.0.9z
APP_NAME=python-flask-mock-rest-apiz

echo AWS Elastic Beanstalk Application: $AWS_ELASTIC_BEANSTALK_APPLICATION
echo AWS Elastic Beanstalk Environment: $AWS_ELASTIC_BEANSTALK_ENVIRONMENT
echo AWS S3 Bucket: $AWS_S3_BUCKET
echo App Version: $APP_VERSION
echo App file: $APP_FILE
echo App name: $APP_NAME

# Copy zip file to S3
#aws s3 cp $APP_FILE $AWS_S3_BUCKET

# Create new application version
#aws elasticbeanstalk create-application-version --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --version-label $APP_VERSION --description $APP_NAME --source-bundle S3Bucket=$BUCKET_NAME,S3Key=$APP_FILE

#update version - do it in update-environ

# Build options.json files
cp options.template.json options.json
sed -i "s/APP_VERSION_VALUE/$APP_VERSION/g" options.json
sed -i "s/APP_NAME_VALUE/$APP_NAME/g" options.json

# Update environment variables
#aws elasticbeanstalk update-environment --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT \
#  --version-label $APP_VERSION \
#  --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=APP_VERSION,Value=$APP_VERSION;Namespace=aws:elasticbeanstalk:application:environment,OptionName=APP_NAME,Value=$APP_NAME

#  aws elasticbeanstalk update-environment --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT \
#    --option-settings '[{"Namespace":"aws:elasticbeanstalk:application:environment","OptionName":"jeff","Value":"$APP_NAME"}]'

aws elasticbeanstalk update-environment --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT \
    --option-settings '[{"Namespace":"aws:elasticbeanstalk:application:environment","OptionName":"jeff","Value":"$APP_NAME"}]'
aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro,m1.medium" "Name=availability-zone,Values=us-west-2c"

# uses .json file for config values
#aws elasticbeanstalk update-environment --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT --option-settings file://options.json
#aws elasticbeanstalk update-environment --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT --option-settings file://options.json
