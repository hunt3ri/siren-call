#!/usr/bin/env bash

echo Running shippable deploy current branch is $BRANCH

# We don't want to deploy Pull Requests only builds on develop and master
if [ $IS_PULL_REQUEST == true ]
    then
        echo Not Deploying Build $BUILD_NUMBER - Branch is $BRANCH, Is Pull Request is $IS_PULL_REQUEST
        return
fi


# Only deploy to Staging if we're on develop
if [ $BRANCH == "develop" ]
    then
        echo Please add necessary deploy scripts here to deploy to staging environment
fi

# Only deploy to Prod if we're on master
if [ $BRANCH == "master" ]
    then
        # Create a local venv using app only dependencies this will create a smaller deployable
        export PIPENV_IGNORE_VIRTUALENVS=1
        export PIPENV_VENV_IN_PROJECT=true
        pipenv install
        python ./devops/deploy.py --deploy
fi
