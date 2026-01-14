from termcolor import colored


# colored(출력할 문자열, 글자색, 배경색, atts=[스타일])

test = colored(
    "BED",
    "blue",
    "on_red",
    ["bold"]
)

print(test)

