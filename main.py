from window import Window
from objects import Point, Line, Cell
from maze import Maze

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import sys
# @@@ 해답은 sys.setrecursionlimit 으로 재귀함수 깊이 제한 중
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def main():
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    sys.setrecursionlimit(10000)
    # 재귀함수 깊이 제한
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    width = 800
    height = 600
    win = Window(width, height)
    # Window 클래스 초기화

    # @@@ 해답과 동일하게 margin 50, 행 12, 열 16
    margin = 50
    num_rows = 12
    num_cols = 16
    cell_size_x = (width - 2*margin) / num_cols
    cell_size_y = (height - 2*margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    # 미로 생성 및 시각화
    maze.solve()
    # 길 탐색 및 시각화

    win.wait_for_close()
    # 위에서 미로 생성 및 길 탐색이 끝난 후 종료버튼이 눌릴때까지 대기하면서 전체 캔버스 초기화하는 함수


if __name__ == "__main__":
    main()