## Siren-Call
Simple app to call Slack web hook with build notifications.  Deployed as AWS Lambda function.

### Dependencies 
To install the required dependencies:
```.bash
pip install pipenv
pipenv install --dev
pipenv shell
pre-commit install
```
Note the app uses [pre-commit](https://pre-commit.com/) to ensure we automatically run the [black](https://black.readthedocs.io/en/stable/) code formatter and [flake8](http://flake8.pycqa.org/en/latest/) linter before each commit 


### Running the Container
App can be run from within a container, to test deploy etc

```bash
docker-compose run siren-call
cd siren-call
```

### Build and deploy
You can build and deploy locally as follows:
```bash
. ./devops/setenv.sh
python ./devops/build.py
python ./devops/deploy.py <archive.zip>
```
