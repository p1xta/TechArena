import itertools

class Table:
    def __init__(self, num, rows, filter_attributes):
        self.num = num
        self.rows = rows
        self.filter_attributes = filter_attributes

class Join:
    def __init__(self, left_table, right_table, left_attr, right_attr):
        self.left_table = left_table
        self.right_table = right_table
        self.left_attr = left_attr
        self.right_attr = right_attr

    def __repr__(self):
        return f"{{{self.left_table}.{self.left_attr} {self.right_table}.{self.right_attr}}}"

def find_join(joins, t1, t2):
    for j in joins:
        if (j.left_table == t1 and j.right_table == t2) or (j.left_table == t2 and j.right_table == t1):
            return j
    return None

def build_join_trees(joins, tables):
    dp = {}
    # Инициализируем для одиночных таблиц
    for table in tables:
        dp[(table,)] = [str(table)]

    # Перебираем все размеры подмножеств
    for size in range(2, len(tables) + 1):
        # Перебираем все подмножества данного размера
        for subset in itertools.combinations(tables, size):
            dp[subset] = []  # Список для хранения возможных деревьев
            # Разбиваем подмножество на две части и проверяем джоин-предикаты
            for split_point in range(1, len(subset)):
                left_sets = itertools.combinations(subset, split_point)
                for left_set in left_sets:
                    right_set = tuple(x for x in subset if x not in left_set)

                left_key = tuple(sorted(left_set))
                right_key = tuple(sorted(right_set))

                if left_key in dp and right_key in dp:
                    found_join = False;
                    for l in left_key:
                            for r in right_key:
                                join_condition = find_join(joins, l, r)

                    if join_condition:
                        found_join = True;
                        print(f"There is a join between {left_set} and {right_set}")
                        # Для всех комбинаций деревьев из левого и правого поддерева
                        for left_tree in dp[left_key]:
                            for right_tree in dp[right_key]:
                                # Строим дерево для текущего джоина
                                current_tree = f"({left_tree} {right_tree} {join_condition})"
                                dp[subset].append(current_tree)
                # if not found_join:
                #         print(f"No valid join between {left_set} and {right_set}")
        print(f"DP State after processing subset {subset}: {dp[subset]}")

    return dp[tuple(sorted(tables))]
'''
4
3
1 2 a b
1 3 a b
2 4 c d
'''
def scan_cost():
    pass

def nest_loop_inner_cost(left_table, right_table, result_rows):
    return left_table.rows * right_table.rows + result_rows * 0.1

def nest_loop_cross_cost(left_table, right_table, result_rows):
    pass

def hash_join_cost(left_table, right_table, result_rows):
    return left_table.rows * 1.5 + right_table.rows * 3.5 + result_rows

''' INPUT '''
#Таблицы и количество строк в них
number_of_tables = int(input())
tables = [x for x in range(1, number_of_tables+1)]
#number_of_rows_in_tables = [int(x) for x in input().split()]

#Аттрибуты для джоинов
# number_of_attributes = int(input())
# attributes = []
# for i in range(number_of_attributes):
#     table_num, filter_attr, card_value = input().split()
#     attributes.append([int(table_num), filter_attr, int(card_value)])

# #Условия для сканов
# number_of_scan_predicats = int(input())
# scan_preds = []
# for i in range(number_of_scan_predicats):
#     table_num, filter_attr = input().split()
#     scan_preds.append([int(table_num), filter_attr])

#Условия для джоинов
number_of_join_conditions = int(input())
join_conditions = []
for i in range(number_of_join_conditions):
    table_num1, table_num2, join_table1_attr, join_table2_attr = input().split()
    join_conditions.append(Join(int(table_num1), int(table_num2), join_table1_attr, join_table2_attr))

scan_costs = []

# print(number_of_rows_in_tables)
# print(attributes)
print(tables)
print(join_conditions)
possible_trees = build_join_trees(join_conditions, tables)
print(f"Possible join trees ({len(possible_trees)} total):")
for tree in possible_trees:
    print(tree)