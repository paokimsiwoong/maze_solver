from window import Window
from objects import Point, Line


def main():
    win = Window(800, 600)
    # Window 클래스 초기화

    line1 = Line(Point(0,0), Point(800,600))
    line2 = Line(Point(100,100), Point(100,300))
    line3 = Line(Point(100,100), Point(300,100))
    line4 = Line(Point(100,100), Point(300,300))
    # 그릴 line들 초기화
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")
    win.draw_line(line4, "red")
    # draw_line함수들은 win.wait_for_close() 전에 있어야 한다

    win.wait_for_close()
    # 실행 상태 함수 호출


if __name__ == "__main__":
    main()