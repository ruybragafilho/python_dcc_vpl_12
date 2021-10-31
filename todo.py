# -*- coding: utf8

import os

import threading
import requests


class Worker(threading.Thread):

    def __init__(self, id_, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.__id = id_ # isso é o id do livro
        self.__numLinhas = 0
    
    def run(self):
        # Use requests.get para baixar um livro
        # A linha abaixo gera o link para um livro
        # id_ = 1182
        # 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(id_, id_)
        # USE HTTP PARA FUNCIONAR NO MOODLE, NÃO HTTPS
        url = 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(self.__id, self.__id)
        livro = requests.get( url )
        for linha in livro.text.splitlines():
            self.__numLinhas += 1

    def get_result(self):
        # 1. retorna o número de linhas do livro
        #print( 'id: ', self.__id, ' Linhas: ', self.__numLinhas )
        return self.__numLinhas



def crawler():
        
    # Dispara uma thread por id do arquivo
    # Soma o resultado de todas    
    pathArquivo = os.path.join( '.', 'dados', 'ids.txt' )
    thds = []
    with open( pathArquivo ) as inputFile:
        for line in inputFile:
            id = int( line.strip() )
            thds.append( Worker(id) )
        
    for t in thds:
        t.start()
    for t in thds:
        t.join()
    
    somaLinhas = 0
    for t in thds:
        somaLinhas += t.get_result()
    return somaLinhas



print( '\n\n' )

print('Teste Crawler')
print( crawler() )

print( '\n\n' )