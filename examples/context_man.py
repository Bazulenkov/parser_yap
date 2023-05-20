from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE = BASE_DIR / "context_man.txt"


class OpenFile(object):
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        try:
            self.fp = open(self.file, self.flag)
        except (IOError, ValueError):
            self.fp = open(self.file, "w")
        return self.fp

    def __exit__(self, exp_type, exp_value, exc_traceback):
        if exp_type is IOError:
            print("Закрываю файл!")
            self.fp.close()  # Закрываем файл в случае ошибки ввода-вывода.
            # Возвращаем True, чтобы обработать ошибку:
            return True
        print("Закрываю файл!")
        self.fp.close()  # Закрываем файл.


with OpenFile(FILE, "w") as fp:
    fp.write("Здравствуй, файл!")

with OpenFile(FILE, "aa") as fp:
    # a = 4
    # b = 0
    # print(a / b)
    fp.write("Как дела?")

print(fp.closed)
