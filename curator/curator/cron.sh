#/bin/bash

# load env
# . /root/env.sh

# test
echo "$(date): executed script" >> /apps/cron.log 2>&1

# /usr/local/bin/curator --config /apps/curator.yml /apps/clear_oldlog.yml >> /apps/cron.log 2>&1
