import time
import random

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
        seed = None,
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

        self._seed = seed
        # random seed
        if self._seed is not None:
        # test등을 위해 seed가 고정되어야 할때만 maze constructor에 None이 아닌 seed를 입력하고
        # 그러할 때만 random.seed 함수로 seed 고정
            random.seed(self._seed)

        self._cells = []
        # _create_cells()안에서 쓰일 _cells 초기화
        self._create_cells()
        # 미로 생성
        self._break_entrance_and_exit()
        # 출입구 생성
        self._break_walls_r(0,0)
        # 미로 벽 제거
        self._reset_cells_visited()
        # 모든 셀들의 visited를 다시 False로 초기화


    def solve(self):
        # main함수에서 실행될 미로 길 찾기 함수
        # 단순히 재귀함수 _solve_r을 실행하고 그 결과를 반환
        return self._solve_r(0,0)


    def _solve_r(self, i, j):
        # DFS 길찾기 재귀함수
        self._animate()
        # 각 재귀 단계마다 0.05초 텀 두면서 전체 그림 렌더링
        cur = self._cells[i][j]
        cur.visited = True

        if i == self._num_rows - 1 and j == self._num_cols -1:
        # 출구일 경우
            return True
        
        def check_wall(cur, di, dj):
            if di == 1 and not cur.has_bottom_wall:
                return True
            elif di == -1 and not cur.has_top_wall:
                return True
            elif dj == 1 and not cur.has_right_wall:
                return True
            elif dj == -1 and not cur.has_left_wall:
                return True
            return False
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= (i+di) < self._num_rows and 0 <= (j+dj) < self._num_cols and not self._cells[i+di][j+dj].visited and check_wall(cur, di, dj):
            # 해당 방향이 방문된 적 없고, 벽도 없을 때
                cur.draw_move(self._cells[i+di][j+dj])
                # 현재 셀과 다음셀 중심을 잇는 빨간선 그리기
                res = self._solve_r(i+di, j+dj)
                if res:
                # 다음 셀이 출구이거나 출구와 이어질 경우
                    return True
                    # True 반환 및 함수 종료
                cur.draw_move(self._cells[i+di][j+dj], undo=True)
                # 다음 셀로 이어지는 경로는 출구로 이어지지 않으므로 빨간선을 다시 회색선으로 변경

        return False
        # 현재 셀에서 이어지는 모든 경로가 출구와 안 이어지면 False 반환



    def _create_cells(self):
    # 미로를 구성하는 cell들을 생성하고 그 모든 cell들을 그리는 다른 함수를 호출하는 함수
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)


    def _break_entrance_and_exit(self):
        # 출입구 벽 제거
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        # 입구는 0,0 cell의 top wall
        self._draw_cell(0,0)
        exit = self._cells[self._num_rows-1][self._num_cols-1]
        exit.has_bottom_wall = False
        # 출구는 self._num_rows-1, self._num_cols-1 cell의 bottom wall
        self._draw_cell(self._num_rows-1, self._num_cols-1)


    def _break_walls_r(self, i,j):
        # DFS로 미로를 돌아다니면서 지나가는 벽들을 제거하는 함수
        cur = self._cells[i][j]
        cur.visited = True

        while True:
            to_visit = []
            # while 루프 돌때마다 반드시 초기화
            # ∵ to_visit에서 하나만 random.choice로 선택해 DFS를 하고 난 후 while 루프를 다시 돌면
            # 선택된 것 말고도 dfs 과정에서 다른 인접 셀이 visited 된 경우 알아서 새 to_visit에는 빠지게 된다

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= (i+di) < self._num_rows and 0 <= (j+dj) < self._num_cols and not self._cells[i+di][j+dj].visited:
                    to_visit.append((di, dj))

            if len(to_visit) == 0:
            # 인접 셀들이 전부 방문 완료 ==> 더이상 이 셀의 벽이 추가로 없어질 일이 없다
            # ==> 그려도 된다
                self._draw_cell(i,j)
                return
                # 그린 후에는 이 셀의 _break_walls_r while 루프 종료 및 함수 종료를 위해 return 
            
            next_di, next_dj = random.choice(to_visit)
            next = self._cells[i+next_di][j+next_dj]

            if next_di == 1:
                cur.has_bottom_wall = False
                next.has_top_wall = False
            elif next_di == -1:
                cur.has_top_wall = False
                next.has_bottom_wall = False
            elif next_dj == 1:
                cur.has_right_wall = False
                next.has_left_wall = False
            elif next_dj == -1:
                cur.has_left_wall = False
                next.has_right_wall = False
            # 현재 셀과 다음 셀 사이 벽 제거

            self._break_walls_r(i+next_di, j+next_dj)
            # 다음 셀 위치에서 재귀 실행
            

    def _reset_cells_visited(self):
        # cell visited 멤버변수 초기화 함수
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False


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
