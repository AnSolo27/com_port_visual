import re
line = "1,2000"
match = re.findall(r'\d+', line)
#print(match[0] if match else 'Not found')
print(int(match[0]))
print(int(match[1]))