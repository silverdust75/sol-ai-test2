# 클래스 실습 예제
#조건 : 
# 1) 생성자 파라미터 self 제외 4개
# 2) 메서드 총 2개 이상
# 3) 객체 3개 생성

class AI:
    def __init__(self, name, age, good, bad):
        self.name = name
        self.age = age
        self.good = good
        self.bad = bad
    def hello(self):
        print(f"안녕하세요. 저는 {self.name}입니다. {self.age}살입니다.")
    def Good_Bad(self):
        print(f" 장점으로는 {self.good}이 있고, 단점으로는 {self.bad}이(가) 있습니다.")
        
GPT = AI("GPT", 4, "방대한 지식을 이용한 방법제시 밑 자료수집", "불확실한 정보나 날조된 정보의 출력")
Gemini = AI("Gemini", 4, "다른 이들보다도 더 많은 지식과 정보", "무분별한 수입으로 인한 저작권 무시")
Perplexity = AI("Perplexity", 4, "다른 이들보다 더 정확한 정보", "과거 기사를 무단으로 도용한 사건을 일으킨적")


GPT.hello()
Gemini.hello()
Perplexity.hello()

GPT.Good_Bad()
Gemini.Good_Bad()
Perplexity.Good_Bad()
