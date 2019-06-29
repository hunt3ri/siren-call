## Siren-Call
Simple app to call Slack web hook with build notifications.  Deployed as AWS Lambda function.

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
