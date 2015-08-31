# -*- coding: utf-8 -*-

from time import sleep
from flask import Flask
from utils import cached

app = Flask(__name__)


@app.route('/')
@cached(timeout=100)
def index():
    sleep(1)
    return 'index'


@app.route('/product')
@cached(timeout=100)
def product():
    sleep(1)
    return 'product'


@app.route('/buy', methods=['POST'])
def buy():
    sleep(1)
    return 'buy'


if __name__ == '__main__':
    app.run()
