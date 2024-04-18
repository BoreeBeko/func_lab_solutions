from tkinter import *
from tkinter.ttk import *
from reactive_handling import *
import app_logger


class App(Tk):
    def __init__(self):
        super().__init__()
        self.tasks_list = get()
        self.draw_frame()
        self.logger = app_logger.get("GUI", "a")
        self.logger.info("GUI created")

    def __del__(self):
        self.logger.warning("GUI destroyed")

    def draw_frame(self):
        # print_todo_list(self.tasks_list)

        # удаление выделенного элемента
        def delete():
            try:
                selection = tasks_listbox.curselection()
                # мы можем получить удаляемый элемент по индексу
                self.tasks_list = remove_task(self.tasks_list, selection[0])
                # print_todo_list(self.tasks_list)
                redraw_listbox()
            except Exception as e:
                self.logger.error(f"{e}")

        # добавление нового элемента
        def add():
            new_task = task_entry.get()
            self.tasks_list = add_task(self.tasks_list, new_task)
            # print_todo_list(self.tasks_list)
            redraw_listbox()

        def redraw_listbox():
            tasks_listbox.delete(0, END)
            tasks = list_from_observable(self.tasks_list)
            for task in tasks[0]:
                tasks_listbox.insert(END, task)

        root = self
        root.title("TODO App")
        root.geometry("300x250")
        root.columnconfigure(index=0, weight=4)
        root.columnconfigure(index=1, weight=1)
        root.rowconfigure(index=0, weight=1)
        root.rowconfigure(index=1, weight=3)
        root.rowconfigure(index=2, weight=1)

        # текстовое поле и кнопка для добавления в список
        task_entry = Entry()
        task_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
        Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

        # создаем список
        tasks_listbox = Listbox()
        tasks_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)

        Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)


def main():
    app = App()
    app.mainloop()
