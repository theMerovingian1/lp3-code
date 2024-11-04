"""
    Rushikesh Borade BE Comp Roll no 2
    Write a program to implement Huffman Encoding using a greedy strategy. 
"""

import heapq


class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(chars, freq):
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        merged_node = Node(frequency=left_child.frequency +
                           right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def generate_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes


def generate_input_lists(string):
    char_freq_mapping = {}
    for char in string:
        char_freq_mapping[char] = char_freq_mapping.get(char, 0) + 1
    return list(char_freq_mapping.keys()), list(char_freq_mapping.values())


def main():
    while True:
        choice = int(
            input("Enter custom string to encode?: \n1.Yes (1)\n2.No (2)\n"))

        if choice == 1:
            input_string = input("Enter string to encode: ")
            char, freq = generate_input_lists(input_string)
            root = build_huffman_tree(char, freq)
            huffman_codes = generate_huffman_codes(root)

            for char, code in huffman_codes.items():
                print(f"Character: {char}, Code: {code}")

        elif choice == 2:
            chars = ['a', 'b', 'c', 'd', 'e', 'f']
            freqs = [5, 9, 12, 13, 16, 45]
            root = build_huffman_tree(chars, freqs)
            huffman_codes = generate_huffman_codes(root)

            print(huffman_codes)
        else:
            print("Invalid choice")

        continue_or_not = input(
            "Continue? (y): yes, (n): no\n").strip().lower()
        if continue_or_not != 'y':
            break


if __name__ == "__main__":
    main()
