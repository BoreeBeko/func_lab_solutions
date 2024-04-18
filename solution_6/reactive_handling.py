from rx import *
import rx.operators as ops
from app_logger import get


logger = get("reactive_handling", "a")


def create_todo_list():
    logger.info("Creating todo_list")
    return create(lambda observer, _: observer.on_next([]))


def add_task(todo_list: Observable, task):
    logger.info("Adding task")
    return todo_list.pipe(
        ops.map(lambda lst: lst + [task])
    )


def mark_task_as_completed(todo_list: Observable, index):
    logger.info("")
    return todo_list.pipe(
        ops.map(lambda lst: lst[:index] + lst[index + 1:])
    )


def remove_task(todo_list: Observable, index: int):
    logger.info("Removing task")
    return todo_list.pipe(
        ops.map(lambda lst: lst[:index] + lst[index + 1:])
    )


def remove_all_tasks(todo_list: Observable):
    return todo_list.pipe(
        ops.map(lambda lst: [])
    )


def print_todo_list(todo_list):
    logger.info("Printing todo_list")
    return todo_list.subscribe(
        lambda lst: print("Todo List:", lst)
    )


def list_from_observable(todo_list: Observable):
    logger.info("Listing from todo_list")
    tasks = []
    todo_list.subscribe(
        on_next=lambda i: tasks.append(i),
    )
    return tasks


def get():
    main_todo_list = create_todo_list()
    return main_todo_list
