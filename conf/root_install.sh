#! /usr/bin/env bash

source $CONF_PATH/functions.sh


function missing() {
    if dpkg -s $1 >/dev/null 2>/dev/null; then
        return 1
    else
        return 0
    fi
}

function apt_install(){
if missing $1; then
    echo_info "Installing $1..."
    sudo apt-get install $1 -y
fi
}

pip_install() {
    if [ -z $(pip-2.7 freeze 2>/dev/null | grep $1) ]; then
        echo_info "Installing $1..."
        if [ -n "$2" ]; then
            sudo pip-2.7 install $2
        else
            sudo pip-2.7 install $1
        fi
    fi
}

apt_install mysql-server
apt_install python-setuptools
apt_install python-dev
apt_install build-essential
apt_install uwsgi
apt_install uwsgi-plugin-python

if [ -z $(which pip-2.7) ]; then
    sudo python2.7 $CONF_PATH/get-pip.py
fi

#pip_install virtualenv==1.9.1 $PYTHON_PACKAGES/virtualenv-1.9.1.tar.gz
