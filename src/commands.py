EMPTY_COMMAND = "ошибка: пустая команда"
UNKNOWN_COMMAND = "ошибка: неизвестная команда: "


class CommandResult:
    """Результат через вывод output и/или флаг выхода из программы"""
    def __init__(self, output: str, should_exit: bool = False) -> None:
        self.output = output
        self.should_exit = should_exit

"""Собрать строку имя команды и её аргументов"""
def format_str(name: str, args: list[str]) -> str:
    if not args:
        return name
    return f"{name} {' '.join(args)}"

"""Выполнить команду или вернуть текст ошибки"""
def execute(command: str, args: list[str]) -> CommandResult:
    if command == "":
        return CommandResult(EMPTY_COMMAND)
    if command == "exit":
        return CommandResult("", should_exit=True)
    if command == "ls":
        return CommandResult(format_str("ls", args))
    if command == "cd":
        return CommandResult(format_str("cd", args))
    message = UNKNOWN_COMMAND + command
    return CommandResult(message)
