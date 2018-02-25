import unittest
from funcs import *

class TestCases(unittest.TestCase):
    #def test(self):
        #self.assertEqual(x, y)
    def test_puzzle_to_grid_1(self):
        self.assertEqual(puzzle_to_grid('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv'),
                                  ['abcdefghij',
                                   'klmnopqrst',
                                   'uvwxyzabcd',
                                   'efghijklmn',
                                   'opqrstuvwx',
                                   'yzabcdefgh',
                                   'ijklmnopqr',
                                   'stuvwxyzab',
                                   'cdefghijkl',
                                   'mnopqrstuv'])
    def test_puzzle_to_grid_2(self):
        self.assertEqual(puzzle_to_grid('0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'),
                                  ['0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                   '0123456789',
                                  ])
    def test_find_indexes_1(self):
        self.assertEqual(find_indexes('****DOG***DOG', 'DOG'), [4, 10])
    def test_find_indexes_2(self):
        self.assertEqual(find_indexes('CAT**CAT*CAT**CACAT**', 'CAT'), [0, 5, 9, 16])
    def test_reverse_1(self):
        self.assertEqual(reverse(['0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789',
                                  '0123456789']),
                                  ['9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210',
                                   '9876543210'])
    def test_reverse_2(self):
        self.assertEqual(reverse(['abcdefghij',
                                  'klmnopqrst',
                                  'uvwxyzabcd',
                                  'efghijklmn',
                                  'opqrstuvwx',
                                  'yzabcdefgh',
                                  'ijklmnopqr',
                                  'stuvwxyzab',
                                  'cdefghijkl',
                                  'mnopqrstuv']),
                                  ['jihgfedcba',
                                   'tsrqponmlk',
                                   'dcbazyxwvu',
                                   'nmlkjihgfe',
                                   'xwvutsrqpo',
                                   'hgfedcbazy',
                                   'rqponmlkji',
                                   'bazyxwvuts',
                                   'lkjihgfedc',
                                   'vutsrqponm'
                                  ])
    def test_rotate_ccw_1(self):
        self.assertEqual(rotate_ccw(['0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789']),
                                     ['9999999999',
                                      '8888888888',
                                      '7777777777',
                                      '6666666666',
                                      '5555555555',
                                      '4444444444',
                                      '3333333333',
                                      '2222222222',
                                      '1111111111',
                                      '0000000000'])
    def test_diamond_45_1(self):
        self.assertEqual(diamond_45(['0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789',
                                     '0123456789']),
                                     ['9',
                                      '89',
                                      '789',
                                      '6789',
                                      '56789',
                                      '456789',
                                      '3456789',
                                      '23456789',
                                      '123456789',
                                      '0123456789',
                                      '012345678',
                                      '01234567',
                                      '0123456',
                                      '012345',
                                      '01234',
                                      '0123',
                                      '012',
                                      '01',
                                      '0'])
    def test_check_forward_row_1(self):
        self.assertEqual(check_forward_row(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'SLO'), [[7, 2, '(FORWARD)']])
    def test_check_forward_row_2(self):
        self.assertEqual(check_forward_row(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'UNIX'), [[9, 3, '(FORWARD)']])
    def test_check_backward_row_1(self):
        self.assertEqual(check_backward_row(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'VIM'), [[1, 4, '(BACKWARD)']])
    def test_check_forward_col_1(self):
        self.assertEqual(check_forward_col(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'CALPOLY'), [[1, 0, '(DOWN)']])
    def test_check_backward_col_1(self):
        self.assertEqual(check_backward_col(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'COMPILE'), [[6, 8, '(UP)']])
    def test_check_diagonal_1(self):
        self.assertEqual(check_diagonal(puzzle_to_grid('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), 'CPE'), [[1, 0, '(DIAGONAL)']])




if __name__ == '__main__':
    unittest.main()
