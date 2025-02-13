import time

from objects import Point, Cell

class Maze():
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        # @@@ Maze의 모든 멤버 변수들 앞에 _ 사용하기
        self._p = Point(x,y)
        # 미로 왼쪽 위 꼭지점
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        # _win은 Window 클래스 인스턴스

        self._cells = []
        # _create_cells()안에서 쓰일 _cells 초기화
        self._create_cells()


    def _create_cells(self):
    # 미로를 구성하는 cell들을 생성하고 그 모든 cell들을 그리는 다른 함수를 호출하는 함수
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)

    
    def _draw_cell(self, i, j):
    # i행 j열 cell의 멤버함수 draw를 호출하는 함수
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if self._win is None:
            return
        # 해답처럼 window 클래스에 문제가 있을 때의 예외 처리 하기
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        cur = self._cells[i][j]
        # i행 j열 cell
        p1 = self._p + Point(self._cell_size_x * j, self._cell_size_y * i)
        p2 = self._p + Point(self._cell_size_x * (j+1), self._cell_size_y * (i+1))
        cur.draw(p1, p2)
        # cell 그리기
        self._animate()

    def _animate(self):
    # _animate 함수는 불릴때마다 _win.redraw()를 해서 이 순간 알고리즘이 어느 위치에서 탐색 중인지 시각화한다
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if self._win is None:
            return
        # 해답처럼 window 클래스에 문제가 있을 때의 예외 처리 하기
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self._win.redraw()
        time.sleep(0.05)
        # 각 호출마다 일정 시간 텀을 두어 사람이 변화하는 모습을 볼 수 있도록 한다
