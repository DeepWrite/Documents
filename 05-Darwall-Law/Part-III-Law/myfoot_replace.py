import re
import os

# 사용자 입력 받기
input_filename = input("입력 파일명(.md 포함): ").strip()
counter_start = int(input("시작 번호: ").strip())

# 출력 파일명: 원래 파일명 + "-mymark.md"
base, ext = os.path.splitext(input_filename)
output_filename = f"{base}-mymark{ext}"

def replacer(match):
    global counter_start
    replacement = f"[^{counter_start}]"
    counter_start += 1
    return replacement

# 파일 읽기
with open(input_filename, "r", encoding="utf-8") as f:
    content = f.read()

# \myfoot 을 찾아 [^번호]로 대체
new_content = re.sub(r'\\myfoot', replacer, content)

# 결과 저장
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"변환 완료! 출력 파일: {output_filename}")
