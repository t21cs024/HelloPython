'''
Created on 2023/10/13

@author: t21cs024
'''
import unittest
import Player

class PlayerTest(unittest.TestCase):
    def testName(self):
        name = 'A'
        playerA = Player.Player(name)
        self.assertEqual(name, playerA.get_name())
        
    def testHand(self):
        playerA = Player.Player('A')
        self.assertTrue(0 <= playerA.show_hand() <=2)
    
    def testWincount(self):
        playerA = Player.Player('A')
        playerA.notify_result(True)
        self.assertEqual( 1, playerA.get_wincount() )
        playerA.notify_result(False)
        self.assertEqual( 1, playerA.get_wincount() )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world’
        self.assertEqual(s.split(), ['hello', 'world’])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
s.split(2)
if __name__ == '__main__’:
unittest.main()

