#!/usr/bin/env bash
# Setup global params.  Must be run prior negotiating with AWS
# Run as follows:
# . ./setenv.sh

# Override defaults if desired
REGION="us-east-1"
PROFILE="hunter_ops"

printf "#####################################\n"
printf "Iain Hunter Ops\n\n"

printf "Clean up Windows weirdness on utils ...\n\n"
dos2unix  ~/.aws/credentials

printf "\nSetting Tooling vars...\n"

export AWS_DEFAULT_PROFILE=$PROFILE
printf "\nawscli default provider:    $PROFILE \n"

printf "#####################################\n"

# push environment onto command line - so easy to see what we're using
# help is here https://www.digitalocean.com/community/tutorials/how-to-customize-your-bash-prompt-on-a-linux-vps
export PS1='\n${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \e[0;36m[$TF_VAR_profile]\n\[\033[00m\]\$ '
