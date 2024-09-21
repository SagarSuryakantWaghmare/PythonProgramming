import multiprocessing
def my_func():
    print("Hello from process",multiprocessing.current_process().name)
process=multiprocessing.Process(target=my_func)     
if __name__ == '__main__':
 process.start()
 process.join()