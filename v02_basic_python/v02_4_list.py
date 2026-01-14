# 리스트 값 변경과 조작
# 특징 : 순서, 수정, 중복 허용

colors = ["red", "green", "blue", "black"]


# 1. 인덱싱
#print(colors[0]) # red
#print(colors[-1]) # black -1은 맨 마지막 값이 나옴

# 2. 슬라이싱
#print(colors[0:2]) # ['red', 'green'] 2번의 바로 앞까지 나옴
#print(colors[0:-1]) # ['red', 'green', 'blue'] 이것도 
#블랙의 앞인 블루까지 나옴
#print(colors[1:-1]) # ['green', 'blue']

# 3. 값 변경
# print(colors[-1]) # black
# colors[-1] = "white"
# print(colors[-1]) # white

# 4. 값 추가
#colors.append("pink") # ['red', 'green', 'blue', 'black', 'pink']
# 어펜드는 맨 뒤에 추가됨
#print(colors)

# 5. 값 추가2
# colors.insert(윛, 값)
# colors.insert(0, "white")
# print(colors) #['white', 'red', 'green', 'blue', 'black']

# 6. 값 제거
# colors.remove("white") #['red', 'green', 'blue', 'black']
# print(colors)

numbers = [6, 4, 5, 3, 9, 8, 7]
# 7. 정렬
# numbers.sort() #sort는 오름차순 정렬
# print(numbers) #[3, 4, 5, 6, 7, 8, 9]
# numbers.sort(reverse=True) # reverse=True는 내림차순 
# True에서 t는 꼭 대문자
# print(numbers)

# 8. 뒤집기
#numbers.reverse() # [9, 8, 7, 6, 5, 4, 3]
#print(numbers)

# 9. 리스트 요소 포함 여부 확인
# print(10 in numbers) # False
# print(3 in numbers) # True