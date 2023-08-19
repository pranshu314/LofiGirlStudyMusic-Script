#!/bin/bash

p_id_mpv=$(ps -ef | grep "mpv --no-terminal --no-video https://www.youtube.com/watch?v=" | grep -v grep | awk '{print $2}')
# p_id_mpv=$1
exec kill -9 $p_id_mpv
