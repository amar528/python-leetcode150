from unittest import TestCase

from matrix.valid_sudoko_36 import Solution


class TestSolution(TestCase):
    def test_is_valid_sudoku_example1(self):
        board = \
             [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        sol = Solution()
        result = sol.isValidSudoku(board)

        self.assertTrue(result)

    def test_is_valid_sudoko_example2(self):
        board = \
             [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        sol = Solution()
        result = sol.isValidSudoku(board)

        self.assertFalse(result)

    def test_is_valid_sudoko_example320(self):
        board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
                 ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["3", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["5", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["9", ".", ".", ".", ".", ".", ".", ".", "."]]

        sol = Solution()
        result = sol.isValidSudoku(board)

        self.assertTrue(result)