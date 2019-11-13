#!/usr/bin/env python -O
# -*- coding: utf-8 -*-

import os


def conf():
    d = {
        "user": os.environ.get('TEST_USER', 'root'),
        "host": os.environ.get('TEST_HOST', 'localhost'),
        "database": os.environ.get('TEST_DATABASE', 'testp'),
        "port": int(os.environ.get('TEST_PORT', '3306'))
    }
    if os.environ.get('TEST_PASSWORD'):
        d["password"] = os.environ.get('TEST_PASSWORD')
    return d