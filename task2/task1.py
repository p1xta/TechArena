import numpy

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

''' INPUT '''

number_of_tables = int(input())
number_of_rows_in_tables = [int(x) for x in input().split()]
number_of_attributes = int(input())
attributes = []
for i in range(number_of_attributes):
    table_num, filter_attr, card_value = input().split()
    attributes.append([int(table_num), filter_attr, int(card_value)])

number_of_scan_predicats = int(input())
scan_preds = []
for i in range(number_of_scan_predicats):
    table_num, filter_attr = input().split()
    scan_preds.append([int(table_num), filter_attr])
    
number_of_join_predicats = int(input())
join_preds = []
for i in range(number_of_join_predicats):
    table_num1, table_num2, join_table1_attr, join_table1_attr = input().split()
    join_preds.append([int(table_num1), int(table_num2), join_table1_attr,join_table1_attr])

''' COSTS '''
scan_costs = []
#popa

print(number_of_rows_in_tables)
print(attributes)