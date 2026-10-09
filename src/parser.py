"""Разбор введённой строки на команду и аргументы."""


def parse_line(line: str) -> tuple[str, list[str]]:
    parts = line.split()
    if not parts:
        return "", []
    return parts[0], parts[1:]
