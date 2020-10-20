# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/


def copyRandomList(head):
    if not head:
        return None

    new_root, id_to_new_node = copy_linked_list_without_random(head)
    fill_randoms_field(head, new_root, id_to_new_node)

    return new_root


def copy_linked_list_without_random(ori_node):
    new_root = new_node = Node(ori_node.val)
    id_to_new_node = {id(ori_node): new_node}
    ori_node = ori_node.next
    while ori_node:
        new_node.next = Node(ori_node.val)
        id_to_new_node[id(ori_node)] = new_node.next
        ori_node = ori_node.next
        new_node = new_node.next

    return new_root, id_to_new_node


def fill_randoms_field(ori_node, new_node, id_to_new_node):
    while ori_node:
        rand_id = id(ori_node.random)
        new_node.random = id_to_new_node[rand_id] if rand_id in id_to_new_node else None
        ori_node = ori_node.next
        new_node = new_node.next
