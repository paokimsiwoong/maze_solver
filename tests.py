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
            maze = Maze(case[0], case[1], case[2], case[3], case[4], case[5])
            self.assertEqual(
                len(maze._cells),
                # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # num_cols,
                case[2], # == num_rows
                # 설명은 _cells가 열, 행 순이지만,
                # 내 코드는 행, 열 순으로 했으므로 변경 필요
                # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            )
            self.assertEqual(
                len(maze._cells[0]),
                case[3],
            )
    
    
    def test_break_entrance_and_exit(self):
        cases = [
            (0, 0, 12, 10, 10, 10),
            (50, 50, 12, 16, 30, 30),  
        ] # 각 case는 (x,y, num_rows, num_cols, cell_size_x, cell_size_y)

        for case in cases:
            maze = Maze(case[0], case[1], case[2], case[3], case[4], case[5])
            self.assertEqual(False, maze._cells[0][0].has_top_wall)
            # 입구부분 wall이 제대로 False인지 확인
            self.assertEqual(False, maze._cells[case[2]-1][case[3]-1].has_bottom_wall)
            # 출구부분 wall이 제대로 False인지 확인

    
    def test_break_walls_r(self):
        pass


    def test_reset_cells_visited(self):
        cases = [
            (0, 0, 12, 10, 10, 10, 0),
            (50, 50, 12, 16, 30, 30, 10),  
        ] # 각 case는 (x,y, num_rows, num_cols, cell_size_x, cell_size_y, seed)

        for case in cases:
            maze = Maze(case[0], case[1], case[2], case[3], case[4], case[5], seed=case[6])
            for i in range(case[2]):
                for j in range(case[3]):
                    self.assertEqual(False, maze._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()