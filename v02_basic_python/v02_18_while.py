# 미터를 피트로 변환하는 함수 + 예외 처리

#함수 정의
def meters_to_feet(meters):
    feet = meters * 3.28084
    '''
    미터(metsers) 단위를 피트(ft) 단위로 변환합니다.

    Args:
        mt (float): 변환하고자 하는 킬로그램 값.

    Returns:
        float: 변환된 파운드 값 (1meters = 3.28084ft 기준).
    '''
    feet = meters * 3.28084
    return feet

#사용자 입력

while True:
    user_input = input("미터 값을 입력해주세요. : ")
    try:
        meters = float(user_input)
        feet = meters_to_feet(meters)
        print(f"{meters}m는 {feet}ft 입니다.")
        break
    except ValueError:
        print("숫자를 입력해주세요. ")
#예외처리
