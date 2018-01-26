#! -*- coding: utf-8 -*-


'''
Created on Jan 26, 2018

@author: Jesús Molina
'''
import sys

class Map(object):
    '''
    classdocs
    '''
    map =     [[0,0,0,0,0,0,0], #0 represents a wall (#), 1 represents the floor (-) and 2 is the hero(@).
               [0,2,1,1,1,1,0],
               [0,1,1,1,1,1,0],
               [0,1,1,1,1,1,0],
               [0,0,0,0,0,0,0]]
    
    
    def generateMap(self): #converts the integers of map into ASCII symbols.
        for x in range(len(self.map)):
            print "\n"
            for y in range(len(self.map[x])):
                if self.map[x][y] == 0:
                    sys.stdout.write('#')#wall.
                    sys.stdout.write(' ') #I had to insert spaces between each symbol, so the map won't be deformed on the screen.
                elif self.map[x][y] == 2:
                    sys.stdout.write('@') #@ is the hero's symbol.
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('-')#floor.
                    sys.stdout.write(' ')
    