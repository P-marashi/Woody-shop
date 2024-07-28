#!/bin/sh

echo "--> Starting web process"

rm -rf /tmp/celeryd.pid
celery -A example.tasks worker -l info -c 5 \
  --without-gossip \
  --without-mingle \
  --without-heartbeat \
  --pidfile=/tmp/celeryd.pid
