# termcolor를 활용한 텍스트 출력 함수 실습
import pyfiglet

def good_sentence(sentence:str):
    '''
    함수 설명:
        입력된 문자열을 pyfiglet 형식으로 출력합니다.
    매개 변수:
        sentence (str): 출력할 문자열
    '''
    py_sentence = pyfiglet.figlet_format(sentence)
    print(py_sentence)


good_sentence("BED")