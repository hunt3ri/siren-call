#!/usr/bin/env python3
import subprocess
import sys


def deploy_lambda_function(app_archive):
    """ Use AWS CLI to deploy"""
    #aws lambda update-function-code --function-name siren-call --s3-bucket code-commit-build-artifacts --s3-key siren-call/iain.zip --publish
    subprocess.run(["aws", "lambda", "update-function-code", "--function-name", "siren-call", "--s3-bucket", "code-commit-build-artifacts", "--s3-key", f"siren-call/{app_archive}", "--publish"])


if __name__ == "__main__":
    """ Helper to deploy app to lambda function"""
    try:
        app_archive = sys.argv[1]
    except IndexError:
        sys.stderr.write("app_archive .zip not supplied ")
        sys.exit(1)

    deploy_lambda_function(app_archive)
