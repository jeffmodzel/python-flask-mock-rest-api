#
# Deploy the zip file to an existing AWS Elastic Beanstalk app/environment
#

# Update the variables to match your environment
echo Deploy to AWS
BUCKET_NAME=elasticbeanstalk-us-east-1-134953076769
AWS_S3_BUCKET=s3://$BUCKET_NAME
AWS_ELASTIC_BEANSTALK_ENVIRONMENT=PythonTest2-env
AWS_ELASTIC_BEANSTALK_APPLICATION=python-test2
APP_VERSION=1.2./d.0
APP_NAME=python-flask-mock-rest-api
APP_FILE=$APP_NAME$APP_VERSION.zip

echo AWS Elastic Beanstalk Application: $AWS_ELASTIC_BEANSTALK_APPLICATION
echo AWS Elastic Beanstalk Environment: $AWS_ELASTIC_BEANSTALK_ENVIRONMENT
echo AWS S3 Bucket: $AWS_S3_BUCKET
echo App Version: $APP_VERSION
echo App name: $APP_NAME
echo App file: $APP_FILE

# Build zip file
# Remove files that aren't related to python application, keep our zip small
zip -r $APP_FILE . -x *.git* *.sh *.zip *_pycache_* *.pytest_cache* *.json *.md *.png postman/\*

# Copy zip file to S3
aws s3 cp $APP_FILE $AWS_S3_BUCKET

# Create new application version
aws elasticbeanstalk create-application-version --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --version-label $APP_VERSION --description $APP_NAME --source-bundle S3Bucket=$BUCKET_NAME,S3Key=$APP_FILE

# Build options.json file - bit of a hack, no easier and cleaner way to update the json file with values from this shell script
cp options.template.json options.json
sed -i "s/APP_VERSION_VALUE/$APP_VERSION/g" options.json
sed -i "s/APP_NAME_VALUE/$APP_NAME/g" options.json

# Update environment
aws elasticbeanstalk update-environment --application-name $AWS_ELASTIC_BEANSTALK_APPLICATION --environment-name $AWS_ELASTIC_BEANSTALK_ENVIRONMENT --version-label $APP_VERSION --option-settings file://options.json
