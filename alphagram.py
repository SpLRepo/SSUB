from typing import Callable

class Alpha:
    def on_message(command, hl):
        async def decor(_, m, *args, **kwargs):
            return
        return decor
