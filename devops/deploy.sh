#!/usr/bin/env bash

echo Running shippable deploy current branch is $BRANCH

# We don't want to deploy Pull Requests only builds on develop and master
if [ $IS_PULL_REQUEST == true ]
    then
        echo Not Deploying Build $BUILD_NUMBER - Branch is $BRANCH, Is Pull Request is $IS_PULL_REQUEST
        return
fi

# Only deploy to Staging if we're on develop
if [ $BRANCH == "add-logging" ]
    then
         export PIPENV_IGNORE_VIRTUALENVS=1
         export PIPENV_VENV_IN_PROJECT=true
         pipenv install
         DIST_FILE=`python ./devops/build.py`
         aws lambda update-function-code --function-name siren-call --s3-bucket code-commit-build-artifacts --s3-key siren-call/$DIST_FILE --publish
fi

# Only deploy to Prod if we're on master
if [ $BRANCH == "master" ]
    then
        echo Please add necessary deploy scripts here to deploy to prod environment
fi