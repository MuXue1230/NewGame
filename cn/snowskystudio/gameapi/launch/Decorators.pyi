from typing import Any, Callable, Self

from cn.snowskystudio.newgame.test.Logger import Logger


class Decorators:
    class LauncherLogger:
        logger: Logger
        launcher: Callable
        def __init__(self, launcher: Callable) -> Self: ...
        def __call__(self, args: int, argv: list) -> Callable: ...
