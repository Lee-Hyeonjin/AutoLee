import sys
import dbconn
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AutoLee Loading...')  # 타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300)  # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(400, 200)  # 위젯의 크기를 너비 400px, 높이 200px로 조절
        self.show()  # 위젯을 스크린에 보여줌


a = dbconn()
print(a.cursor)
if __name__ == '__main__':  # 현재 모듈의 이름이 저장되는 내장 변수
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()


# sys.exit(app.exec_())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print(dir())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
