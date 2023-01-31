from typing import Callable

class Alpha:
    def on_message(command, hl, *args):
        async def decor(_, m):
            return
        return decor
