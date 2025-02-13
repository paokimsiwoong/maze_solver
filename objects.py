class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @@@@@
    # Point 클래스 활용하기 위해 연산자 override
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, factor):
        if isinstance(factor, int) or isinstance(factor, float):
            return Point(self.x * factor, self.y * factor)
        raise TypeError("Factor must be either int or float")
    def __rmul__(factor, self):
        if isinstance(factor, int) or isinstance(factor, float):
            return Point(self.x * factor, self.y * factor)
        raise TypeError("Factor must be either int or float")
    # def __div__(self, factor):
    # @@@@@@@ python3부터는 truediv 사용 @@@@@@@
    def __truediv__(self, factor):
        if isinstance(factor, int) or isinstance(factor, float):
            if factor != 0:
                return Point(self.x / factor, self.y / factor)
            raise ZeroDivisionError()
        raise TypeError("Factor must be either int or float")


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # p1, p2는 Point 클래스

    
    # def draw(self, canvas, fill_color):
    def draw(self, canvas, fill_color="black"):
    # @@@ 해답처럼 fill_color 기본값 지정하기
        # canvas(tkinter.Canvas)를 받아서 그 canvas에 fill_color색 선을 그리는 함수
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        # p1, p2를 잇는 선 그리기


class Cell():
    def __init__(self, window=None, p1=None, p2=None, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        # 사방 벽이 있는지 없는지 - 기본 True
        self._p1 = p1
        self._p2 = p2
        # @@@ 기본 None, draw 함수 input p1,p2를 저장하기
        self._win = window
        # _win == Window클래스 인스턴스

        self.visited = False
        # visited는 해당 cell 인스턴스의 벽들이 제거되었는지 아닌지 여부 체크
    

    def draw(self, p1:Point, p2:Point, fill_color="black"):
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if self._win is None:
            return
        # 해답처럼 window 클래스에 문제가 있을 때의 예외 처리 하기
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # p1을 왼쪽 위 꼭지점, p2를 오른쪽 아래 꼭지점으로 두는 cell 그리는 함수 
        self._p1 = p1
        self._p2 = p2
        # @@@ 해답처럼 멤버 변수 _p1, _p2 갱신하기
        if self.has_left_wall:
            self._win.draw_line(line= Line(p1, Point(p1.x, p2.y)), fill_color=fill_color)
            # Window클래스의 draw_line 함수 사용
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
        # 이전에 벽이 있어서 fill_color로 그린 후 벽이 제거된 경우
        # else에서 아무것도 하지 않으면 기존에 그린 벽이 남아 있어 제거된 것이 보이지 않는다
        # ===> 배경색으로 아예 새로 그려서 지우는 효과를 만들기
            # self._win.draw_line(line= Line(p1, Point(p1.x, p2.y)), fill_color="white")
            self._win.draw_line(line= Line(p1, Point(p1.x, p2.y)), fill_color="#d9d9d9") # 배경색이 white가 아니라 #d9d9d9이므로 변경
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if self.has_right_wall:
            self._win.draw_line(line= Line(Point(p2.x, p1.y), p2), fill_color=fill_color)
        else:
            self._win.draw_line(line= Line(Point(p2.x, p1.y), p2), fill_color="#d9d9d9")
        if self.has_top_wall:
            self._win.draw_line(line= Line(p1, Point(p2.x, p1.y)), fill_color=fill_color)
        else:
            self._win.draw_line(line= Line(p1, Point(p2.x, p1.y)), fill_color="#d9d9d9")
        if self.has_bottom_wall:
            self._win.draw_line(line= Line(Point(p1.x, p2.y), p2), fill_color=fill_color)
        else:
            self._win.draw_line(line= Line(Point(p1.x, p2.y), p2), fill_color="#d9d9d9")



    def draw_move(self, to_cell, undo=False):
        # 현재 cell 인스턴스 중심점에서 to_cell 중심점까지 선을 그리는 함수
        # undo가 False이면 red, True이면 gray 색상 선택
        fill_color = "gray" if undo else "red"
        self._win.draw_line(line= Line((self._p1 + self._p2) /2, (to_cell._p1 + to_cell._p2) /2), fill_color=fill_color)

# @@@ 해답 draw_move
#     def draw_move(self, to_cell, undo=False):
#         half_length = abs(self._x2 - self._x1) // 2
#         # x2보다 x1이 큰 경우도 대비해 abs 함수 사용
#         x_center = half_length + self._x1
#         y_center = half_length + self._y1
#         # cell 실제 중심이 아니라 x축 기준 절반 길이를 y축에도 사용


#         half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
#         x_center2 = half_length2 + to_cell._x1
#         y_center2 = half_length2 + to_cell._y1

#         fill_color = "red"
#         if undo:
#             fill_color = "gray"

#         line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
#         self._win.draw_line(line, fill_color)