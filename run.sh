#!/bin/bash

CONT="iredteam"

docker stop $CONT 2>/dev/null
docker rm $CONT 2>/dev/null

docker run -d --name $CONT -p 4000:3000 djangobyjeffrey/iredteam
