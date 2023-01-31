from typing import Callable

class Alpha:
    def on_message(self, args*):
        async def decor(_, m):
            return
        return decor
