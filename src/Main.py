'''
Created on Dec 23, 2014

@author: ubuntu
'''

from Simulator import Simulator
from time import sleep

if __name__ == '__main__':
    sim = Simulator()
    sim.Start()
    sleep(15)
    sim.stop()
    