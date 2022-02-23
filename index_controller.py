from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class IndexController(ControllerBase):
    pass


def get():
    name = "Tony Joy"
    return render_template('index.html', name=name)
