"""
This sub is used to set up logging for pop projects and injects logging
options into conf making it easy to add robust logging
"""
# Import python libs
import logging


def __init__(hub):
    """
    Set up variables used by the log subsystem
    """
    logging.addLevelName(5, "TRACE")
    hub.log.LOGGER = {
        # Initialize the root logger
        "": logging.getLogger()
    }
    hub.log.LEVEL = {
        "notset": logging.NOTSET,
        "trace": 5,
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warn": logging.WARN,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "fatal": logging.FATAL,
        "critical": logging.CRITICAL,
    }

    # These should be overwritten by the integrated logger, but here's a contingency
    hub.log.INT_LEVEL = logging.INFO
    hub.log.log = hub.log.LOGGER[""].log
    hub.log.trace = lambda *args, **kwargs: hub.log.LOGGER[""].log(5, *args, **kwargs)
    hub.log.debug = hub.log.LOGGER[""].debug
    hub.log.info = hub.log.LOGGER[""].info
    hub.log.critical = hub.log.LOGGER[""].critical
    hub.log.warning = hub.log.LOGGER[""].warning
    hub.log.error = hub.log.LOGGER[""].error


def conf(hub, name):
    """
    Return the conf dict for logging, this should be merged OVER by the loaded
    config dict(s)
    """
    # TODO: Make this more robust to handle more logging interfaces
    ldict = {
        "log_file": {
            "default": f"{name}.log",
            "help": "The location of the log file",
            "group": "Logging Options",
        },
        "log_level": {
            "default": "info",
            "help": "Set the log level, either quiet, info, warning, or error",
            "group": "Logging Options",
        },
        "log_fmt_logfile": {
            "default": "%(asctime)s,%(msecs)03d [%(name)-17s][%(levelname)-8s] %(message)s",
            "help": "The format to be given to log file messages",
            "group": "Logging Options",
        },
        "log_fmt_console": {
            "default": "[%(levelname)-8s] %(message)s",
            "help": "The log formatting used in the console",
            "group": "Logging Options",
        },
        "log_datefmt": {
            "default": "%H:%M:%S",
            "help": "The date format to display in the logs",
            "group": "Logging Options",
        },
        "log_plugin": {
            "default": "basic",
            "help": "The logging plugin to use",
            "group": "Logging Options",
        },
    }
    return ldict
