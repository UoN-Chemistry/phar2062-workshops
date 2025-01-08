#!/usr/bin/env sh
pip install build &&\
python -m build &&\
pip install dist/*.whl &&\
rm -rf dist *.egg-info
