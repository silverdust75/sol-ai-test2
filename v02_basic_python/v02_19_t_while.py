#kg => 1b 변환 프로그램(입력 반복, 예외 처리)
# def, while, try, except 사용.

def kg_to_b(kg):
    b = kg * 2.20462
    '''
    킬로그램(kg) 단위를 파운드(lb) 단위로 변환합니다.

    Args:
        kg (float): 변환하고자 하는 킬로그램 값.

    Returns:
        float: 변환된 파운드 값 (1kg = 2.20462lb 기준).
    '''
    b = kg * 2.20462
    return b

while True:
    user_input = input("값을 입력해 주세요. : ")
    try:
        kg = float(user_input)
        b = kg_to_b(kg)
        print(f"{kg}kg는 {b}pound입니다. ")
        break
    except ValueError:
        print("숫자를 입력해 주세요.")
        