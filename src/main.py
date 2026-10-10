"""Графический интерфейс эмулятора"""

import tkinter as tk
from tkinter import scrolledtext

from commands import execute
from config import Config, parse_args
from parser import parse_line
from script import read_script, run_line, script_commands

VFS_NAME = "VFS"
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 460
OUTPUT_HEIGHT = 20
PREFIX = "> "
HELP_LINE = "Команды: ls, cd, exit"


class ShellApp:
    """Окно"""

    def __init__(self, vfs_name: str, config: Config) -> None:
        """Инициализация характеристик окна"""
        self.config = config
        self.root = tk.Tk()
        self.root.title(vfs_name)
        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )
        self.output = scrolledtext.ScrolledText(
            self.root,
            height=OUTPUT_HEIGHT,
            state="disabled",
            wrap="word",
        )
        self.output.pack(fill="both", expand=True, padx=8, pady=8)
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill="x", padx=8, pady=(0, 8))
        self.entry.bind("<Return>", self.on_submit)
        self.entry.focus_set()
        self.write(HELP_LINE)
        self.root.after(0, self.show_startup)

    def show_startup(self) -> None:
        """Показать параметры и выполнить стартовый скрипт"""
        for line in self.config.debug_lines():
            self.write(line)
        if self.config.script_path == "":
            return
        self.play_script(self.config.script_path)

    def play_script(self, path: str) -> None:
        """Выполнить скрипт или вывести ошибку"""
        lines, error = read_script(path)
        if error != "":
            self.write(error)
            return
        for line in script_commands(lines):
            if self.run_shown(line):
                return

    def run_shown(self, line: str) -> bool:
        """Показать строку и ответ. Вернуть True, если это exit"""
        self.write(PREFIX + line)
        result = run_line(line)
        if result.output != "":
            self.write(result.output)
        if result.should_exit:
            self.root.destroy()
        return result.should_exit

    def run(self) -> None:
        """Запустить цикл окна"""
        self.root.mainloop()

    def on_submit(self, _event: tk.Event) -> None:
        """Записать введённую строку и выполнить команду"""
        line = self.entry.get()
        self.entry.delete(0, "end")
        self.write(PREFIX + line)
        command, args = parse_line(line)
        result = execute(command, args)
        if result.output:
            self.write(result.output)
        if result.should_exit:
            self.root.destroy()

    def write(self, text: str) -> None:
        """Вставить строку в область вывода"""
        self.output.configure(state="normal")
        self.output.insert("end", text + "\n")
        self.output.configure(state="disabled")
        self.output.see("end")


def main() -> None:
    """Открыть окно"""
    ShellApp(VFS_NAME, parse_args()).run()


if __name__ == "__main__":
    main()
