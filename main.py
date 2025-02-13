from window import Window
from objects import Point, Line, Cell
from maze import Maze


def main():
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

    win.wait_for_close()
    # 실행 상태 함수 호출


if __name__ == "__main__":
    main()