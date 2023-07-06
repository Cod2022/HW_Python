from task3 import task1_write_numbers as wn, task2_names_generation as ng, task3_write_file as wf

wn.int_float_write(10, 'numbers.txt')
ng.names_gen(5, 'names.txt')
wf.write_new_file('names.txt', 'numbers.txt', 'names_numbers.txt')
