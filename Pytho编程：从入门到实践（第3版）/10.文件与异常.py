from pathlib import Path

# 相对路径
path = Path('assets/pi_digits.txt')
context = path.read_text()
print(context.strip())

lines = context.splitlines()
num = ''
for line in lines:
    # 文件解析默认都是字符串
    num += line.strip()

print(num)