#! -*- coding: utf-8 -*-

'''
Created on Jan 25, 2018

@author: Jesús Molina
'''


from tittleScreen.tittleScreen import TittleScreen
from map.map import Map


if __name__ == '__main__':
    
        tittle = TittleScreen()
        tittle.startScreen()
        
        myMap = Map()
        myMap.generateMap()
        
        