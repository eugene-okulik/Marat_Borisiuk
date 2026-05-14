import argparse
import os
import re
import sys
from colorama import init, Fore, Style

init()

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Путь к папке с логами")
parser.add_argument("--text", required=True, help="Текст для поиска")

args = parser.parse_args()

log_path = args.path
search_text = args.text.lower()

if not os.path.exists(log_path):
    print(f"{Fore.RED}Ошибка: путь {log_path} не существует{Style.RESET_ALL}")
    sys.exit(1)

if not os.path.isdir(log_path):
    print(f"{Fore.RED}Ошибка: {log_path} — укажите путь к папке{Style.RESET_ALL}")
    sys.exit(1)

date_pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}"

for filename in os.listdir(log_path):
    file_path = os.path.join(log_path, filename)
    if not os.path.isfile(file_path) or not filename.endswith(".log"):
        continue

    with open(file_path, "r") as f:
        lines = f.readlines()

    blocks = []
    current_block_lines = []
    current_date = None
    start_line = 0

    for i, line in enumerate(lines, 1):
        if re.match(date_pattern, line):
            if current_block_lines:
                blocks.append(
                    {
                        "date": current_date,
                        "text": "\n".join(current_block_lines),
                        "line": start_line,
                    }
                )
            current_date = line.strip()[:23]
            current_block_lines = [line.strip()]
            start_line = i
        else:
            if current_block_lines:
                current_block_lines.append(line.strip())

    if current_block_lines:
        blocks.append(
            {
                "date": current_date,
                "text": "\n".join(current_block_lines),
                "line": start_line,
            }
        )

    for block in blocks:
        if search_text in block["text"].lower():
            print(f"{Fore.GREEN}Найдено в файле: {filename}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Строка: {block['line']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Время ошибки: {block['date']}{Style.RESET_ALL}")

            words = block["text"].split()
            for j, word in enumerate(words):
                if search_text in word.lower():
                    found = True
                    start = max(0, j - 5)
                    end = min(len(words), j + 6)
                    fragment = " ".join(words[start:end])
                    print(f"Контекст: ... {fragment} ...")
            print("-" * 50)
