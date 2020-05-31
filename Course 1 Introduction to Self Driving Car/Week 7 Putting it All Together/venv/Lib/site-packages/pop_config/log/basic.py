import inspect
import logging
import pop.contract
import sys


def _stack_frames(relative_start: int) -> inspect.FrameInfo:
    """
    Efficiently access stack frames.
    :param relative_start: Starting stack depth; The default, 2 is the parent of the
                           caller of stack_frames - the first function that may be unknown.
    :return: a stack frame
    """
    if hasattr(sys, "_getframe"):
        # implementation detail of CPython, speeds things up by 100x.
        frame = sys._getframe(relative_start)
        while frame:
            yield frame
            frame = frame.f_back
    else:
        for frame_info in inspect.stack(context=0)[relative_start:]:
            yield frame_info.frame


def _get_hub_ref() -> str:
    # Minimize lookup time by starting at frame 5, it will be at least that far back
    for frame in _stack_frames(5):
        if isinstance(frame.f_locals.get("self"), pop.contract.Contracted):
            contracted = frame.f_locals["self"]
            break
    else:
        # Default to the root reference
        return "hub"

    return contracted.func.__module__


def _get_logger(hub, name: str = "") -> logging.Logger:
    if name not in hub.log.LOGGER:
        hub.log.LOGGER[name] = logging.getLogger(name)
    return hub.log.LOGGER[name]


def log(hub, level: int, msg: str, *args, **kwargs):
    if hub.log.INT_LEVEL <= level:
        caller = _get_hub_ref()
        logger = _get_logger(hub, caller)
        logger.log(level, msg, *args, **kwargs)


def trace(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.log(5, msg, *args, **kwargs)


def debug(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.debug(msg, *args, **kwargs)


def info(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.info(msg, *args, **kwargs)


def critical(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.critical(msg, *args, **kwargs)


def warning(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.warning(msg, *args, **kwargs)


def error(hub, msg: str, *args, **kwargs):
    caller = _get_hub_ref()
    logger = _get_logger(hub, caller)
    logger.error(msg, *args, **kwargs)


def null(hub, *args, **kwargs):
    """
    A logging level that eats log messages, this is because the functions defined above
    call `_get_hub_ref` which cat be expensive, especially if `sys` doesn't
    have the `_get_frame` function.
    """


def setup(hub, conf):
    """
    Given the configuration data set up the logger
    """
    raw_level = conf["log_level"].strip().lower()
    if raw_level.isdigit():
        hub.log.INT_LEVEL = int(raw_level)
    else:
        hub.log.INT_LEVEL = hub.log.LEVEL.get(raw_level, logging.DEBUG)

    # Use the saved root logger
    root = _get_logger(hub)
    root.setLevel(hub.log.INT_LEVEL)
    cf = logging.Formatter(fmt=conf["log_fmt_console"], datefmt=conf["log_datefmt"])
    ch = logging.StreamHandler()
    ch.setLevel(hub.log.INT_LEVEL)
    ch.setFormatter(cf)
    root.addHandler(ch)
    ff = logging.Formatter(fmt=conf["log_fmt_console"], datefmt=conf["log_datefmt"])
    fh = logging.FileHandler(conf["log_file"])
    fh.setLevel(hub.log.INT_LEVEL)
    fh.setFormatter(ff)
    root.addHandler(fh)

    hub.log.log = hub.log.basic.log
    for log_level in ("trace", "debug", "info", "critical", "warning", "error"):
        if hub.log.INT_LEVEL <= hub.log.LEVEL[log_level]:
            hub.log.basic.debug(f"Setting up {log_level} logging")
            # Set up logging at a low level on the hub
            setattr(hub, f"log.{log_level}", getattr(hub, f"log.basic.{log_level}"))
        else:
            hub.log.basic.debug(f"Ignoring {log_level} logging")
            # Override the logger with the null logger if we aren't at that level.
            # This significantly reduces unnecessary big-O complexity when we don't need logging
            setattr(hub, f"log.{log_level}", hub.log.basic.null)
