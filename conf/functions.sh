#! /usr/bin/env bash


echo_info() {
    echo -e "\033[0;32;1m$1\033[0m"
}

echo_warning() {
    echo -e "\033[0;33;1m$1\033[0m"
}

echo_error() {
    echo -e "\033[0;31;1m$1\033[0m"
}


virtualenv --distribute .pyenv

source $ROOT_PATH/.pyenv/bin/activate

pip install -r $CONF_PATH/requirements.txt \
    -i=http://g.pypi.python.org/simple/ \
    -d $PYTHON_PACKAGES --no-install


pip install -r $CONF_PATH/requirements.txt \
    --find-links=file://$PYTHON_PACKAGES \
    --no-index

v_is_install() {
    if [ -d $VENV_PATH ]; then
        return 0
    else
        return 1
    fi
}

v_install() {
    $VENV_BIN $VENV_PATH
    v_activate
    upgrade
}

v_activate() {
    source "$VENV_PATH/bin/activate"
}

upgrade() {
    v_activate
    command pip install -r $CONF_PATH/requirements.txt \
        --find-links=file://$PYTHON_PACKAGES \
        --no-index
    if [ -n "$(uwsgi --json 2>&1|grep 'unrecognized')" ]; then
        command pip install -U uwsgi \
            --find-links=file://$PYTHON_PACKAGES \
            --no-index
    fi
}

pip() {
    if [[ $1 == "install" ]]; then
        command pip $@ \
            --index-url=http://g.pypi.python.org/simple/ \
            --download=$PYTHON_PACKAGES --no-install
        command pip $@ \
            --find-links=file://$PYTHON_PACKAGES \
            --no-index
        freeze
    else
        command pip $@
    fi
}

seeyou() {
    deactivate
    unset ROOT_PATH
    unset CONF_PATH
    unset VENV_BIN
    unset VENV_PATH
    unset PYTHON_PACKAGES
}
