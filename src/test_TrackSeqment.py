'''
Created on Dec 23, 2014

@author: ubuntu
'''
import unittest
from TrackSegment import TrackSegment
from Station import Station
from Train import Train

class TrackSeqmentTest(unittest.TestCase):

    def setUp(self):
        self.station = Station('B')
        self.trackSegment = TrackSegment('A-B', self.station)

    def testName(self):
        self.assertEqual('A-B', self.trackSegment.name)
        
    def testAddTrain(self):
        train = Train(1, 1, 't')
        self.trackSegment.add_train(train)
        self.assertEqual(1, self.trackSegment.num_of_trains())
    
    def testRoute(self):
        train = Train(1, 1, 't')
        self.trackSegment.add_train(train)
        self.trackSegment._route()
        self.assertEqual(1, self.station.num_of_docked_trains())

if __name__ == "__main__":
    unittest.main()