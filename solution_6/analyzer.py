# Функция для чтения файла логов и анализа его содержимого
def analyze_logs(log_file):
    # Открываем файл логов
    with open(log_file, 'r') as file:
        # Считываем все строки из файла
        log_lines = file.readlines()

        # Пример анализа: подсчет числа строк
        num_lines = len(log_lines)
        print("Всего строк в логе:", num_lines)

        # Пример анализа: поиск строк, содержащих определенное слово
        word_to_search = 'warning'
        warning_lines = [line for line in log_lines if word_to_search in line.lower()]
        num_warnings = len(warning_lines)
        print("Количество строк с ошибками:", num_warnings)

        # Пример анализа: поиск строк, содержащих определенное слово
        word_to_search = 'error'
        error_lines = [line for line in log_lines if word_to_search in line.lower()]
        num_errors = len(error_lines)
        print("Количество строк с ошибками:", num_errors)


# Вызов функции с указанием пути к файлу логов
log_file_path = 'app_logger.log'
analyze_logs(log_file_path)
