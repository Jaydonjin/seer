#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

# ----------------------------------------
# deploy app manually
# replace DEPLOY_SERVER with the release server
#
# sirius docker_deploy:seer,${IMAGE},server=DEPLOY_SERVER,ports="9201;8080"
# -----------------------------------------

# ----------------------------------------
# deploy app into GDEV apps cluster
# you should not care about the app's tcp port
# ---------------------------------------

sirius docker_dev_deploy:seer,${IMAGE}
