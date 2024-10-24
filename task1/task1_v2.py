from collections import defaultdict

class Table:
    def __init__(self, num, rows, filter_attributes):
        self.num = num
        self.rows = rows
        self.cost = 0
        self.filter_attributes = filter_attributes

class Join:
    def __init__(self, left_table, right_table, left_attr, right_attr):
        self.left_table = left_table
        self.right_table = right_table
        self.left_attr = left_attr
        self.right_attr = right_attr

    def __repr__(self):
        return f"{{{self.left_table}.{self.left_attr} {self.right_table}.{self.right_attr}}}"

def build_join_graph(joins):
    graph = defaultdict(list)
    for join in joins:
        # Добавляем ребро между таблицами
        graph[join.left_table].append((join.right_table, join))
        graph[join.right_table].append((join.left_table, join))
    return graph

def build_trees(graph, current_table, used_tables, current_tree):
    if len(used_tables) == len(graph):
        # Если все таблицы задействованы, возвращаем текущее дерево
        return [current_tree]
    
    trees = []
    # Проходим по всем соседям (возможные джоины) для текущей таблицы
    for neighbor, join_condition in graph[current_table]:
        if neighbor not in used_tables:
            # Добавляем соседа в дерево и продолжаем рекурсивное построение
            # new_joins_in_tree = joins_in_tree + [str(join_condition)]
            # new_used_tables = used_tables | {neighbor}
            # trees.extend(build_trees(graph, neighbor, new_used_tables, new_joins_in_tree))
            new_used_tables = used_tables | {neighbor}
            new_tree = f"({current_table} {neighbor} {join_condition}) {current_tree}"
            trees.extend(build_trees(graph, neighbor, new_used_tables, new_tree))
    
    return trees

def build_join_trees(joins, tables):
    # Создаем граф джоинов
    join_graph = build_join_graph(joins)
    all_trees = []
    
    # Начинаем с каждой таблицы и строим деревья
    for table in tables:
        all_trees.extend(build_trees(join_graph, table, {table}, str(table)))
    
    return all_trees

'''
4
3
1 2 a b
1 3 a b
2 4 c d
'''

''' INPUT '''
#Таблицы и количество строк в них
number_of_tables = int(input())
tables = [x for x in range(1, number_of_tables+1)]
#number_of_rows_in_tables = [int(x) for x in input().split()]


#Условия для джоинов
number_of_join_conditions = int(input())
join_conditions = []
for i in range(number_of_join_conditions):
    table_num1, table_num2, join_table1_attr, join_table2_attr = input().split()
    join_conditions.append(Join(int(table_num1), int(table_num2), join_table1_attr, join_table2_attr))

scan_costs = []

# print(number_of_rows_in_tables)
# print(attributes)
# print(tables)
# print(join_conditions)
possible_trees = build_join_trees(join_conditions, tables)
print(f"Possible join trees ({len(possible_trees)} total):")
for tree in possible_trees:
    print(tree)