from dataclasses import dataclass

RESET = "\033[0m"

# Foreground color codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


@dataclass
class Configs:
    BINARY_PATH: str = ""
    SERVER_ADDRESS = ("localhost", 3113)
    WORKSPACE: str = ""
    USE_BINARY: bool = False
    USE_TCP: bool = False
    IS_DEBUGGING: bool = False


configs = Configs()


async def get_configs() -> Configs:
    return configs


"""
A dictionary that controls the debugging behavior of the application.

@keys: response methods
@values: boolean values that control the debugging behavior of the application.
"""
debug_method_map = {
    "debug/message": True,
    "webview/postMessage": True,
}


async def get_debug_map():
    return debug_method_map
