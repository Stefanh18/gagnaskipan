class _DoublyLinkedBase:
     
    class _Node:

        def __init__(self):
            self._header = self._Node(None, None, None)
            self._trailer = self._Node(None, None, None)
            self._header._next = self._trailer
            self._trailer.prev = self._header
            self._size = 0

        def __len__(self):
            return self._size