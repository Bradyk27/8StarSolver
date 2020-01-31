class Node():
    def __init__(self, parent_node = None, node_position = None):
        self.parent_node = parent_node
        self.node_position = node_position

        self.distance = 0
        self.heuristic = 0
        self.total_cost = self.distance + self.heuristic


    def __eq__(self, other):
        return self.position = other.position


def a_star(tree, start, end):
        
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        closed_list.append(open_list.pop(current_index))

        if current_node = end_node:
            path = []
            current = current_node

            while current is not None:
                path.append(current.node_position)
                current = current.parent
            return path [::1]


        children = []
        for index, number in current_node.node_position:
            if number == 0:
                blank_index = index

        if index = 0: #Logic here is sound, test it. Also, memory management?
            child = copy.deepcopy(current_node)
            current_node.node_position[0], current_node.node_position[1] = child.node_position[1], child.node_position[0]
            children.append(child)

            child = copy.deepcopy(current_node) #Replicate this for all applicable nodes. Children will ALWAYS be +- 1 or +- 3
            current_node.node_position[0], current_node.node_position[3] = child.node_position[3], child.node_position[0]
            children.append(child)

        if index = 1:
            children.append([0,1,2,3,4,5,6,7,8]
            children.append([1,2,0,3,4,5,6,7,8]
            children.append([1,4,2,3,0,5,6,7,8]

        if index = 2:
                            
                

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.distance = current_node.distance + 1
            child.heuristic = current_node.heuristic #Draw up a heuristic algorithm
            child.total_cost = child.distance + child.heuristic

            for open_node in open_list:
                if child == open_node and child.distance > open_node.distance:
                    continue

            open_list.append(child)



def main():
    eight_puzzle = []

    start = [1,2,3,4,5,6,7,8]
    end = [1,2,3,4,5,6,7,8,0]
    path = a_star(eight_puzzle, start, end)
    print(path)



main()
