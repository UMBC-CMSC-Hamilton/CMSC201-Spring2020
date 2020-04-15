def sum_goal_buggy(my_list, goal):
    """
    :param my_list: list of numbers
    :param goal: goal to be added up
    :return: True if some sublist adds to goal, False else
    """
    if goal == 0:
        return True
    else:
        # ignore my_list[0]
        if sum_goal_buggy(my_list[1:], goal):
            return True
        # include my_list[0] in the sum
        elif sum_goal_buggy(my_list[2:], goal + my_list[0]):
            return True
        return False
