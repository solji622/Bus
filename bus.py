from kivy.app import App #앱 모듈 불러오기
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('bus.kv')

class Main(Screen):
    pass

class BusApp(App): #메인 앱 클래스 선언(괄호 안에 모듈 상속)
    def build(seif): #이 함수에서 return 하는 것이 만드려는 앱
        sm = ScreenManager()
        sm.add_widget(Main(name='main'))
        return sm

if __name__ == '__main__': 
    BusApp().run() #run() 함수 실행하여 앱 구동
