#!/bin/sh

# screenの名前
SCREEN_NAME='mini'

if [ -n "$(screen -list | grep -o "${SCREEN_NAME}")" ]; then
    # 停止コマンド発行
    screen -S $SCREEN_NAME -X stuff 'geyser stop\015'
    #停止実行待機
    sleep 30s
else
    echo [date '+%F %T']  'server is not runnning'
fi
