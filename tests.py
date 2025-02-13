import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cases = [
            (0, 0, 12, 10, 10, 10),
            (50, 50, 12, 16, 30, 30),             
        ]
        # 각 case는 (x,y, num_rows, num_cols, cell_size_x, cell_size_y)

        for case in cases:
            m1 = Maze(case[0], case[1], case[2], case[3], case[4], case[5])
            self.assertEqual(
                len(m1._cells),
                # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # num_cols,
                case[2], # == num_rows
                # 설명은 _cells가 열, 행 순이지만,
                # 내 코드는 행, 열 순으로 했으므로 변경 필요
                # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            )
            self.assertEqual(
                len(m1._cells[0]),
                case[3],
            )


if __name__ == "__main__":
    unittest.main()