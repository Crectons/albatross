#!/bin/bash

uwsgi --reload uwsgi.pid
service nginx reload
celery multi restart w1 -B -A OccupationSwitch -l info
