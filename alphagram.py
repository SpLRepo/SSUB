from typing import Callable

class Alpha:
    def on_message(func: Callable):
        async def decor(_, m):
            return
        return decor
