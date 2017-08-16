#!/bin/bash
set -e

show_help() {
  echo """
  Commands
  test          : run tests
  gen_docs      : generate docs
  start_dev     : start django dev server
  start_jupyter : start jupyter notebook
  manage        : run django manage.py
  eval          : eval shell command
  bash          : run bash
  """
}

export PYTHONPATH="/opt/app:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE=eduproject.settings

case "$1" in
  "test" )
    export TESTING=true
    # Linting tasks first
    flake8 ./
    # Then tests
    ./scripts/wait_for_dbs.sh
    # Run python tests and pass on any args to e.g. run individual tests
    ./manage.py test --exclude-tag selenium "${@:2}"
  ;;
  "gen_docs" )
    ./scripts/gen_docs.sh
  ;;
  "start_dev" )
    export DEV_SERVER=true
    export SHOW_DEBUG_TOOLBAR=true
    ./scripts/gen_docs.sh
    ./manage.py migrate --noinput
    ./manage.py runserver 0.0.0.0:8080
  ;;
  "start_jupyter" )
    jupyter notebook -y --no-browser --ip=0.0.0.0 --config=/opt/notebooks/jupyter_notebook_config.py --notebook-dir=/opt/notebooks/
  ;;
  "manage" )
    ./manage.py "${@:2}"
  ;;
  "eval" )
    eval "${@:2}"
  ;;
  "bash" )
    bash
  ;;
  * )
    show_help
  ;;
esac
