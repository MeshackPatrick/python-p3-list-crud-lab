def create_an_empty_list():
    my_list = []
    return my_list


def create_a_list():
    my_list = ["shercie", "wesh", "memer", "sherciewesh"]
    return my_list


def add_element_to_end_of_list(my_list, memerwesh):
    my_list.append(memerwesh)
    return my_list


def add_element_to_start_of_list(my_list, john):
    my_list.insert(0, john)
    return my_list


def remove_element_from_end_of_list(my_list):
    my_list.pop()
    return my_list


def remove_element_from_start_of_list(my_list):
    del my_list[0]
    return my_list


def retrieve_first_element_from_list(my_list):
    my_list = my_list[0]
    return my_list


def retrieve_element_from_index(my_list, index):
    my_list = my_list[2]
    return my_list


def retrieve_last_element_from_list(my_list):
    my_list = my_list[-1]
    return my_list
