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
