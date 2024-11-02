items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def find_item_index(items, item):
    """
    Функция для поиска индекса первого вхождения элемента в списке.

    Args:
        items (list): Список товаров.
        item (str): Товар, который нужно найти.

    Returns:
        int: Индекс первого вхождения товара в списке.
        None: Если товар не найден в списке.
    """
    for i, element in enumerate(items):
        if element == item:

            return i
    return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item) # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")




