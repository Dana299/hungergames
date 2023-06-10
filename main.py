import asyncio

from tasks.A import process_urls
from tasks.B import make_dict
from tasks.C import process_list
from tasks.D import make_n_requests
from tasks.E import TextAnalyzer

task_2A_test_data = [
    "https://github.com/miguelgrinberg/Flask-SocketIO",
    "https://github.com/miguelgrinberg/Flask-SocketIO.git",
    "github.com/miguelgrinberg/Flask-SocketI",
    "https://github.com/miguelgrinberg/Flask/SocketIO",
    "https://github.com/dana299",
]

task_2B_test_data = [
    ['key_D', 'key_C', 'key_A', 'key_B'],
    ['value_1', 'value_2', 'value_3', 'value_4', 'value_5'],
]

task_2C_test_data = [
    "string_1", 4, "string_2", 12, "string_3", 8
]

with open("task_2E_text.txt", 'r') as f:
    task_2E_test_data = f.read()


if __name__ == "__main__":

    print("\n_____TASK_2A_RUNNING_____\n")
    process_urls(task_2A_test_data)

    print("\n_____TASK_2B_RUNNING_____\n")
    print("Test data: ", *task_2B_test_data, sep='\n', end='\n\n')
    print("Result: ", make_dict(*task_2B_test_data))

    print("\n_____TASK_2C_RUNNING_____\n")
    print("Test data: ", task_2C_test_data, end='\n')
    print("Result: ", process_list(task_2C_test_data))

    print("\n_____TASK_2D_RUNNING_____\n")
    asyncio.run(make_n_requests(n=100, url="http://127.0.0.1/delay/3"))

    print("\n_____TASK_2E_RUNNING_____\n")
    analyzer = TextAnalyzer(text=task_2E_test_data)
    analyzer.get_longest()
    analyzer.get_most_common()
    analyzer.get_palyndromes()
    analyzer.get_special_symbols_number()
