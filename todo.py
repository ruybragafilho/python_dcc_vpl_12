# -*- coding: utf8


import threading
import requests


class Worker(threading.Thread):
    def __init__(self, id_, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self._id = id_ # isso é o id do livro
    
    def run(self):
        # Use requests.get para baixar um livro
        # A linha abaixo gera o link para um livro
        # id_ = 1182
        # 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(id_, id_)
        # USE HTTP PARA FUNCIONAR NO MOODLE, NÃO HTTPS
        pass


def crawler():
    # Dispara uma thread por id do arquivo
    # Soma o resultado de todas
    pass