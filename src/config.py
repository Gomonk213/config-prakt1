import argparse

NOT_SET = "не задан"


class Config:
    """Пути к VFS и стартовому скрипту."""

    def __init__(self, vfs_path: str, script_path: str) -> None:
        """Пустая строка значит, что путь не задан."""
        self.vfs_path = vfs_path
        self.script_path = script_path

    def debug_lines(self) -> list[str]:
        """Вывод весх параметров запуска для окна вывода"""
        return [
            "vfs_path=" + self.show(self.vfs_path),
            "script_path=" + self.show(self.script_path),
        ]

    def show(self, value: str) -> str:
        """Возврат параметра и проверка на пустоту"""
        if value == "":
            return NOT_SET
        return value


def parse_args() -> Config:
    """Прочитать --vfs и --script из командной строки"""
    parser = argparse.ArgumentParser(
        description="Эмулятор оболочки",
    )
    parser.add_argument(
        "--vfs",
        default="",
        help="Путь к физическому расположению VFS",
    )
    parser.add_argument(
        "--script",
        default="",
        help="Путь к стартовому скрипту",
    )
    args = parser.parse_args()
    return Config(args.vfs, args.script)
