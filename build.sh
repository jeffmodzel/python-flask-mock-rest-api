echo Build zip file for uploading to AWS

ZIP_FILE=app.zip

if [ -f $ZIP_FILE ]
then
  rm $ZIP_FILE
fi

# Remove files that aren't related to python application, keep our zip small
zip -r $ZIP_FILE . -x .gitignore *.git* *.sh *.zip *_pycache_* *.pytest_cache* *.json *.md
