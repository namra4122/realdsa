from .trie import Trie

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
    ("start_with", "sho", ["shop", "shopping", "show", "showstoper"]),
    ("start_with", "ai", ["air", "airbone"]),
    ("start_with", "ha", ["hash"]),
    ("start_with", 412, [412202, 4122]),
    ("delete", "air", True),
    ("search", "air", False),
    ("delete", "airstrip", False),
    ("delete", "（书、杂志等中区别于图片的）正文，文字材料", True),
    ("search", "（书、杂志等中区别于图片的）正文，文字材料", False),
    ("delete", "hash", True),
    ("search", "hash", True),
    ("delete", 412202, True),
    ("search", 412202, False),
    ("delete", "showstoper", True),
    ("search", "showstoper", False),
    ("delete", "shop", True),
    ("search", "shop", False),
    ("update", (4122, 412202), False),
    ("search", 412202, True),
    ("update", ("show", "showstoper"), False),
    ("search", "showstoper", True),
    ("delete_all", "", None),
]


def test_trie():
    trie = Trie()
    for test_op_str, test_in, test_out in testcases:
        test_op = getattr(trie, test_op_str)
        testoutput = test_op(test_in)
        assert testoutput == test_op
