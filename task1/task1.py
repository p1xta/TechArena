import numpy

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

''' INPUT '''

f = open("input.txt")
number_of_tables = int(f.readline().strip())
number_of_rows_in_tables = [0]
for x in f.readline().strip().split():
    number_of_rows_in_tables.append(int(x))

number_of_attributes = int(f.readline().strip())
attributes = [[] for _ in range(number_of_tables + 1)]
for i in range(number_of_attributes):
    table_num, filter_attr, card_value = f.readline().strip().split()
    attributes[int(table_num)].append([int(table_num), filter_attr, int(card_value)])

number_of_scan_predicats = int(f.readline().strip())
scan_preds = [[] for _ in range(number_of_scan_predicats + 1)]
for i in range(number_of_scan_predicats):
    table_num, filter_attr = f.readline().strip().split()
    scan_preds.append([int(table_num), filter_attr])
    
number_of_join_predicats = int(f.readline().strip())
join_preds = []
for i in range(number_of_join_predicats):
    table_num1, table_num2, join_table1_attr, join_table2_attr = f.readline().strip().split()
    join_preds.append([int(table_num1), int(table_num2), join_table1_attr, join_table2_attr])

'''CALC'''
faster_join_preds = [[*sublist] for sublist in join_preds]
for i in range(number_of_join_predicats):
    if number_of_rows_in_tables[faster_join_preds[i][0]] > number_of_rows_in_tables[faster_join_preds[i][1]]:
        temp = faster_join_preds[i][0]
        faster_join_preds[i][0] = faster_join_preds[i][1]
        faster_join_preds[i][1] = temp
        temp = faster_join_preds[i][2]
        faster_join_preds[i][2] = faster_join_preds[i][3]
        faster_join_preds[i][3] = temp

''' COSTS '''
scan_costs = []

print(number_of_rows_in_tables[2])
print(attributes[2])
print(join_preds)
print(faster_join_preds)