# context manager
# with open('myfilename.txt') as f:
#     pass


class Log_Manager:
    def __enter__(self):
        print('Entering context manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context manager')


class Test_Context_Manager:
    def __enter__(self):
        print('task1')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('task2')


def do_task():
    print("do task")

# with Log_Manager():
#     do_task()

with (
    Log_Manager() as ctx1,
    Test_Context_Manager() as ctx2,
):
    do_task()