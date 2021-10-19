import sys

console_input = sys.argv[1]

word_list = console_input.split(' ')
output = word_list[0]
output = output.replace(',', '')
print(output)
