import unittest  ### testy jednostek
import ConwaysGameOfLife

class TestGameOfLife( unittest.TestCase ):

    def test_count_neighbours(self):
        neighbours = [  0, 1, 0, 1,   0, 1, 0, 0  ]
        self.assertEqual(  3,  ConwaysGameOfLife.count_neighbours( neighbours )  )

    def test_is_alive(self):       # def is_alive(  was_alive,  num_neighbours  )
        self.assertFalse( ConwaysGameOfLife.is_alive(  True,  0  ) ) # stop life
        self.assertFalse( ConwaysGameOfLife.is_alive(  True,  1  ) ) # stop life
        self.assertFalse( ConwaysGameOfLife.is_alive(  True,  4  ) ) # stop life

        self.assertFalse( ConwaysGameOfLife.is_alive(  False, 2  ) ) # remain death
        self.assertFalse( ConwaysGameOfLife.is_alive(  False, 4  ) ) # remain death

        self.assertTrue ( ConwaysGameOfLife.is_alive(  True,  2  ) ) # STAY ALIVE
        self.assertTrue ( ConwaysGameOfLife.is_alive(  True,  3  ) ) # STAY ALIVE
        self.assertTrue ( ConwaysGameOfLife.is_alive(  False, 3  ) ) # BORN TO LIFE


    def test_get_sixteen_neighbours(self):
        board    = [   [   [1, 1, 0],  [0, 9, 1],  [0, 0, 0]   ],
                       [   [1, 1, 0],  [0, 9, 1],  [0, 0, 0]   ],
                       [   [1, 1, 0],  [0, 9, 1],  [0, 0, 0]   ]   ]
        expected = [        1, 1, 0 ,   0, 9, 1 ,   0, 0, 0     ,
                            1, 1, 0 ,   0,    1 ,   0, 0, 0     ,
                            1, 1, 0 ,   0, 9, 1 ,   0, 0, 0        ]
        self.assertEqual(  expected,  ConwaysGameOfLife.get_ei8ht_neighbours( board, 1, 1 )  )
    def test_get_sixteen_neighbours__lewy(self):
        board    = [   [   [2873641, "asdfsjdf", 3],  [4, 5, 6],  [7, 8, 9]   ],
                       [   [2873641, "asdfsjdf", 3],  [4, 5, 6],  [7, 8, 9]   ],
                       [   [2873641, "asdfsjdf", 3],  [4, 5, 6],  [7, 8, 9]   ]   ]
        expected = [        2873641, "asdfsjdf", 3 ,   4, 5, 6 ,   7, 8, 9,
                            2873641, "asdfsjdf", 3 ,   4,    6 ,   7, 8, 9,
                            2873641, "asdfsjdf", 3 ,   4, 5, 6 ,   7, 8, 9        ]
        self.assertEqual(  expected,  ConwaysGameOfLife.get_ei8ht_neighbours( board, 1, 1 )  )



if __name__ == "__main__":
    unittest.main()