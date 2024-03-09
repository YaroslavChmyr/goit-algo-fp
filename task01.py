# Реалізація однозв'язного списку
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
def reverse_linked_list(linked_list: LinkedList):
    prev = None
    cur = linked_list.head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    linked_list.head = prev


# Алгоритм сортування для однозв'язного списку через сортування вставками;
def insertion_sort_linked_list(linked_list: LinkedList):
    sorted_list = LinkedList()
    cur = linked_list.head

    while cur:
        next_node = cur.next
        insert_node = None
        if sorted_list.head is None or sorted_list.head.data >= cur.data:
            cur.next = sorted_list.head
            sorted_list.head = cur
        else:
            insert_node = sorted_list.head
            while insert_node.next and insert_node.next.data < cur.data:
                insert_node = insert_node.next
            cur.next = insert_node.next
            insert_node.next = cur
        cur = next_node

    linked_list.head = sorted_list.head


# Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
def merge_sorted_linked_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    cur1 = list1.head
    cur2 = list2.head

    while cur1 and cur2:
        if cur1.data < cur2.data:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        else:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next

    while cur1:
        merged_list.insert_at_end(cur1.data)
        cur1 = cur1.next

    while cur2:
        merged_list.insert_at_end(cur2.data)
        cur2 = cur2.next

    return merged_list


llist = LinkedList()
llist2 = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(10)
llist.insert_at_beginning(5)
llist.insert_at_beginning(20)
llist.insert_at_beginning(15)
print("Список до реверсування:")
llist.print_list()

# Реверсуємо однозв'язний список
reverse_linked_list(llist)
print("Список після реверсування:")
llist.print_list()

# Сортуємо однозв'язний список
insertion_sort_linked_list(llist)
print("Список після сортування:")
llist.print_list()

# Додаємо вузли до іншого списку
llist2.insert_at_beginning(30)
llist2.insert_at_beginning(25)

# Сортуємо список 2
insertion_sort_linked_list(llist2)

# Об'єднуємо списки
merged_list = merge_sorted_linked_lists(llist, llist2)
print("Об'єднаний список:")
merged_list.print_list()

