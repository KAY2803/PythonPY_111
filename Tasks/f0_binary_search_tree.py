"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

root = {
    "key": 8,
    "value": 8,
    "left": {
        "key": 3,
        "value": 3,
        "left": None,
        "right": None,
    },
    "right": {
        "key": 10,
        "value": 10,
        "left": None,
        "right": None,
    },
}


class BinarySearchTree:
    def __init__(self):
        """
        Example:
        {
            "key": 8,
            "value": 8,
            "left": {
                "key": 3,
                "value": 3,
                "left": None,
                "right": None,
            },
            "right": {
                "key": 10,
                "value": 10,
                "left": None,
                "right": None,
            },
        }
        """

        self.root = None

    @staticmethod
    def _create_node(key, value, left=None, right=None) -> dict:
        """ Фабричный метод для узлов"""
        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """

        def _insert(current_node: Optional[dict]):
            if self.root is None:
                self.root = self._create_node(key, value)
            else:
                current_key = current_node['key']

                if key == current_key:
                    current_node['value'] = value

                if key > current_key:
                    if current_node["right"] is None:
                        current_node["right"] = self._create_node(key, value)  # добавляем лист
                    else:
                        return _insert(current_node["right"])  # спускаемся дальше

                else:
                    if current_node["left"] is None:
                        current_node["left"] = self._create_node(key, value)
                    else:
                        return _insert(current_node["left"])

        return _insert(self.root)

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists
        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """

        def _remove(current_node: Optional[dict]):
            if not self.root or self.root is None or current_node is None:
                return None

            if current_node['key'] == key:
                if current_node['left'] is None and current_node['right'] is None:
                    [current_node.pop(keys) for keys in ['key', 'value', 'left', 'right']]
                elif current_node['right'] is None:
                    [current_node.pop(keys) for keys in ['key', 'value', 'left', 'right']]
                    self.root = current_node['left']
                elif current_node['left'] is None:
                    [current_node.pop(keys) for keys in ['key', 'value', 'left', 'right']]
                    self.root = current_node['right']
                else:
                    while True:
                        min_current_node = current_node['left']
                        current_node['key'] = min_current_node['key']
                        current_node['value'] = min_current_node['value']
                        if min_current_node['left'] is None:
                            [min_current_node.pop(keys) for keys in ['key', 'value', 'left', 'right']]
                            break

            else:
                current_key = current_node['key']
                if key > current_key:
                    return _remove(current_node['right'])
                else:
                    return _remove(current_node['left'])

        return _remove(self.root)

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST
        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        def _find(current_node: Optional[dict]):
            if current_node is None:
                raise KeyError

            if current_node["key"] == key:
                return current_node["value"]

            current_key = current_node["key"]
            # next_node = current_node["right"] if key > current_key current_node["left"]
            # _find(next_node)
            if key > current_key:
                return _find(current_node["right"])
            else:
                return _find(current_node["left"])

        return _find(self.root)

    def clear(self) -> None:
        """
        Clear the tree
        :return: None
        """
        if self.root is None:
            return None
        self.root.clear()