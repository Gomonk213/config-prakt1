"""Обработка скриптов"""
from commands import CommandResult, execute
from parser import parse_line

COMMENT = "#"
READ_ERROR = "ошибка: не удалось прочитать скрипт: "


def is_comment(line: str) -> bool:
    return line.startswith(COMMENT)


def read_script(path: str) -> tuple[list[str], str]:
    """Вернуть строки файла или текст ошибки чтения, если есть"""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.readlines(), ""
    except OSError:
        return [], READ_ERROR + path


def script_commands(lines: list[str]) -> list[str]:
    """Оставить только команды без пустых строк и комментариев"""
    ready = []
    for line in lines:
        text = line.strip()
        if text == "":
            continue
        if is_comment(text):
            continue
        ready.append(text)
    return ready


def run_line(line: str) -> CommandResult:
    """Разбить одну строку скрипта и выполнить её"""
    command, args = parse_line(line)
    return execute(command, args)
