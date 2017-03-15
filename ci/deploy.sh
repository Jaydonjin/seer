#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

# ----------------------------------------
# deploy app manually
# replace DEPLOY_SERVER with the release server
#
# sirius docker_deploy:seer2,${IMAGE},server=DEPLOY_SERVER,ports="9200;8080",env="ENV\=gqc"
# ----------------------------------------------------------------------------

# ----------------------------------------
# deploy app into GQC apps cluster
# you should not care about the app's tcp port
# ---------------------------------------

sirius docker_dev_deploy:seer2,${IMAGE},env="ENV\=gqc"

[ $? -gt 0 ] && exit 1

# -------------------------------------------
# push release docker image into docker.neg repository

RELEASE_IMAGE=$(sirius docker_image_name:release=true | head -n 1)

docker tag -f ${IMAGE} docker.neg/${RELEASE_IMAGE}

docker push docker.neg/${RELEASE_IMAGE}

[ $? -gt 0 ] && exit 2
# -------------------------------------------

exit 0
