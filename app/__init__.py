#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app # fixme: there is a error
from flask import render_template


@app.route('/')
def index():
	return "Hello World!"

