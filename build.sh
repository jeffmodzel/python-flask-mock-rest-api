echo Build zip file for uploading to AWS

ZIP_FILE=app.zip

if [ -f $ZIP_FILE ]
then
  rm $ZIP_FILE
fi

zip -r $ZIP_FILE . -x .gitignore *.git* *.sh *.zip
