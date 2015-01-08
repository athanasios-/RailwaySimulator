'''
Created on Dec 22, 2014

@author: ubuntu
'''
import unittest
import time
from Cargo import Cargo

class CargoTest(unittest.TestCase):

    def setUp(self):
        self.cargo = Cargo('destination')

    def testLoad(self):
        startTime = time.time()
        self.cargo.load()
        self.assertGreaterEqual(time.time() - startTime, 3)
        
    def testUnload(self):
        startTime = time.time()
        self.cargo.unload()
        self.assertGreaterEqual(time.time() - startTime, 3)
    
    def testDestination(self):
        self.assertEqual('destination', self.cargo.destination, 'train_cargo has destination')


if __name__ == "__main__":
    unittest.main()