# kg to pound 변환하는 함수 실습

def kg_for_pound(kg):
    pound = kg * 2.20462
    return pound

user_input = input("변환할 kg단위를 입력해주세요. :")
kg = float(user_input)
print(type(kg))

pound = kg_for_pound(kg)
print(f"{kg}kg는 {pound}pound입니다.")