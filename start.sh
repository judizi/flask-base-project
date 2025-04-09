#!/bin/bash
RELATIVE_DIR=`dirname "$0"`
cd $RELATIVE_DIR

PRJ_DIR=`pwd`
echo $PRJ_DIR

VENV_DIR=$PRJ_DIR/.venv
PID_FILE=$PRJ_DIR/.backend.pid
RUN_DIR=$PRJ_DIR/backend
REQUIREMENTS_FILE=$RUN_DIR/requirements.txt
APP_PATH=$RUN_DIR/run.py

function install_venv() {
    echo ">> venv does not exist."
    python3 -m venv .venv && source $VENV_DIR/bin/activate && python3 -m pip install -r $REQUIREMENTS_FILE
    if [ $? -ne 0 ]; then
        return 1
    else
        return 0
    fi
}

function kill_process() {
    PARENT_PID=$(cat $PID_FILE)
    CHILD_PIDS=$(pgrep -P "$PARENT_PID")

    for pid in $CHILD_PIDS; do
      kill $pid
    done

    kill $PARENT_PID

    remove_pid
}

function remove_all() {
    rm -rf $VENV_DIR $PID_FILE
}

function remove_pid() {
    rm -rf $PID_FILE
}


if [ -f "$PID_FILE" ]; then
    echo ">> 프로그램을 종료합니다."
    kill_process
    remove_pid
else
    if [ ! -d "$VENV_DIR" ]; then
        install_venv
        if [ $? -ne 0 ]; then
            echo ">> install venv fail.. try again"
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py ; rm -rf get-pip.py
            install_venv
        fi 
    fi

    if [ $? -ne 0 ]; then
        echo ">> venv 설치 실패"
        remove_all
        sleep 3
        exit 1
    fi

    source $VENV_DIR/bin/activate && nohup python3 $RUN_DIR/run.py >/dev/null 2>&1 & echo $! > $PID_FILE
    sleep 3

    if [ $? -ne 0 ] || ! kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
        echo ">> 프로그램을 재시작 해주세요"
        kill_process
        remove_all
    else
        echo ">> 프로그램이 시작되었습니다."
    fi 
fi

echo ">> Press Enter to exit..."
read 
