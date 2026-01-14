import pyfiglet
from termcolor import colored

# 1. 함수 정의
def decorate_text(text, color, font='standard'):
    '''
    1. pyfiglet으로 텍스트를 튜닝
    2. termcolor로 색상 적용
    '''
    py_text = pyfiglet.figlet_format(text, font=font)
    color_py_text = colored(py_text, color)
    return color_py_text

# 2. 함수 호출
decorate_text("GOOD", "red")
print(decorate_text("GOOD", "red"))

last_text = decorate_text("LAST", "yellow")

def box_print(text):
    print("=" * 40)
    print(text)
    print("=" * 40)
    
box_print(last_text)


# 1. 텍스트 출력 완성 
# 2. return을 사용하는 이유
    #1. 
    #2. 