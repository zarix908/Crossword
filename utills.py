from itertools import chain


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def calc_answer_id(node):
    answer_id = node.id

    vertical = node.is_vertical_orientation

    if vertical and 0 in node.incident_nodes:
        incident_node = node.incident_nodes[0]

        if 0 in incident_node.incident_nodes:
            if incident_node.incident_nodes[0] == node:
                answer_id = incident_node.id

    return answer_id


def generate_unfilled_grid_answers(solution):
    horizontal_answers = []
    vertical_answers = []

    for node, word in solution.items():
        answer_id = calc_answer_id(node)
        vertical = node.is_vertical_orientation
        answers = vertical_answers if vertical else horizontal_answers
        answers.append("  " + str(answer_id) + ")" + word + "\n")

    vertical_answers.insert(0, "Vertically:\n")
    horizontal_answers.insert(0, "\nHorizontally:\n")
    return "".join(chain(vertical_answers, horizontal_answers))
