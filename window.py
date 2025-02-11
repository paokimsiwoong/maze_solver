from tkinter import Tk, BOTH, Canvas
# tkinter 라이브러리를 이용해 윈도우 창을 띄우고 조작하기

class Window():
    def __init__(self, width, height, title="Maze Solver"):
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # __를 사용해 멤버 변수들을 모두 private으로
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # self.width = width
        # self.height = height
        # # 윈도우의 가로세로 지정
        # @@@ width, height는 해답처럼 canvas 설정에만 쓰고 따로 저장 안하기
        # self.root = Tk()
        self.__root = Tk()
        # @@@ 해답과 동일하게 private 멤버로 변경
        # root widget
        self.__root.title(title)
        # root widget 타이틀 지정
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # protocol 멤버 함수로 밑에 정의한 close함수를 delete window 액션과 연결


        self.__canvas = Canvas(self.__root, width=width, height=height)
        # 그림이 그려질 Canvas 초기화
        self.__canvas.pack()
        # .pack()함수를 실행해야 이 객체를 창에 표시한다

        self.__is_running = False
        # 이 창이 실행되고 있는지 아닌지 알리는 불 변수


    def redraw(self):
        # 이 함수를 호출해서 렌더링 
        self.__root.update_idletasks()
        self.__root.update()
        # 이 update 함수가 불릴때마다 윈도우에 그림이 새로 그려진다
    
    def wait_for_close(self):
        # self.is_running을 True로 변경 후 이 True가 유지되는 동안 redraw함수를 반복해서 호출하는 함수
        self.__is_running = True

        while self.__is_running:
            self.redraw()

    def close(self):
        # 이 함수가 불리면 self.is_running가 False로 되고
        # 그로 인해 wait_for_close함수 안의 while 루프가 종료된다
        print("Window closed.")
        self.__is_running = False
        
    