from collections import defaultdict
import json
from typing import Optional


class Node:
    def __init__(self):
        self.end_of_word = 0
        self.child = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, data: str | int) -> None:
        curr = self.root
        data = str(data)
        for ch in data:
            curr = curr.child[ch]

        curr.end_of_word += 1

    def delete(
        self,
        data: str | int,
        node: Node | None = None,
    ) -> bool | str:
        if node is None:
            node = self.root

        data = str(data)
        if not len(data):
            if node.end_of_word == 0:
                return False
            node.end_of_word -= 1

            return len(node.child) == 0 and node.end_of_word == 0

        ch = data[0]

        if ch not in node.child.keys():
            return "Not Found"

        should_delete = self.delete(data[1:], node.child[ch])

        if should_delete == True:
            del node.child[ch]

            return node == self.root or (len(node.child) == 0 and node.end_of_word == 0)
        elif should_delete == "Not Found":
            return "Not Found"

        return node == self.root

    def search(self, data: str | int) -> bool:
        data = str(data)
        curr = self.root

        for ch in data:
            if ch not in curr.child.keys():
                return False  # word not in trie
            curr = curr.child[ch]

        return curr.end_of_word > 0

    def update(self, values: tuple) -> bool:
        if self.delete(values[0]):
            self.insert(values[1])
            return True
        return False

    def start_with(self, phrase: str | int) -> list[str]:
        pass

    def delete_all(self) -> None:
        self.root = Node()

    def visualize(self, node: Optional[Node] = None) -> list:
        if node is None:
            node = self.root

        if not node.child:
            return []

        result = []
        for char, child in node.child.items():
            result.append(
                {char: {"children": self.visualize(child), "count": child.end_of_word}}
            )

        return result


testcases = [
    ("insert", "shop", None),
    ("insert", "shopping", None),
    ("insert", "show", None),
    ("insert", "showstoper", None),
    ("insert", "show", None),  # duplicate inser
    ("insert", "stop", None),
    ("insert", "hash", None),
    ("insert", "hash", None),  # duplicate inser)s
    ("insert", "air", None),
    ("insert", "airbone", None),
    ("insert", 412202, None),
    ("insert", 4122, None),
    ("insert", "（书、杂志等中区别于图片的）正文，文字材料", None),
    ("search", "（书、杂志等中区别于图片的）正文，文字材料", True),
    ("search", "sharp", False),
    ("search", "show", True),
    ("search", "airohub", False),
    ("search", "stopping", False),
    ("search", "shop", True),
    ("search", "shopping", True),
    ("search", "stoper", False),
    ("search", 41204, False),
    ("search", 412202, True),
    # ("start_with", "sho", ["shop", "shopping", "show", "showstoper"]),
    # ("start_with", "ai", ["air", "airbone"]),
    # ("start_with", "ha", ["hash"]),
    # ("start_with", 412, [412202, 4122]),
    ("delete", "air", True),
    ("search", "air", False),
    ("delete", "airstrip", "Not Found"),
    ("delete", "（书、杂志等中区别于图片的）正文，文字材料", True),
    ("search", "（书、杂志等中区别于图片的）正文，文字材料", False),
    ("update", ("hash", "namra"), True),
    ("search", "namra", True),
    ("search", "hash", True),
    ("delete", 412202, True),
    ("search", 412202, False),
    ("delete", "showstoper", True),
    ("search", "showstoper", False),
    ("delete", "shop", True),
    ("search", "shop", False),
    ("update", (4122, 412202), True),
    ("search", 412202, True),
    ("update", ("show", "showstoper"), True),
    ("search", "showstoper", True),
]


trie = Trie()


def test_trie():
    for test_op_str, test_in, test_out in testcases:
        print(f"Running Test: {test_op_str} -> {test_in} -> {test_out}")
        test_op = getattr(trie, test_op_str)
        testoutput = test_op(test_in)
        assert testoutput == test_out
    print(json.dumps(trie.visualize()))
