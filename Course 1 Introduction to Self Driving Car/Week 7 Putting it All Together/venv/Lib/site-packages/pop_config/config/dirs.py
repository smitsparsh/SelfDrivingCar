"""
Find the conf.py files specificed in sources
"""
# Import python libs
import importlib
import copy
import secrets
import os


def _load_pyimp(hub, imp):
    """
    Load up a python path, parse it and return the conf dataset
    """
    ret = {imp: {}}
    cmod = importlib.import_module(f"{imp}.conf")
    path = os.path.dirname(cmod.__file__)
    for sec in hub.config.SECTIONS:
        ret[imp][sec] = copy.deepcopy(getattr(cmod, sec, {}))
    return path, ret


def load(hub, sources, dyne_names, cli):
    """
    Look over the sources list and find the correct conf.py files
    """
    # Dynamic names
    # First gather the defined sources, they are the autoritative ones
    # Then ditect what the dynamic names are in the source
    # Merged the sources dyne names with any passed dyne names
    # Load up and extend the raw with all of the dynamic names
    raw = {}
    dyne = hub.pop.dyne.get()
    if not isinstance(sources, list):
        sources = [sources]
    for source in sources:
        try:
            path, data = _load_pyimp(hub, source)
        except ImportError:
            continue
        hub.pop.dicts.update(raw, data)
    dnames = set(dyne_names)
    for source in raw:
        for dname in raw[source]["DYNE"]:
            dnames.add(dname)
    for name in dnames:
        if name in dyne:
            if name not in raw:
                raw[name] = {"CONFIG": {}, "CLI_CONFIG": {}}
            if "CLI_CONFIG" in dyne[name]:
                draw = {}
                cli_draw = {}
                for key, val in dyne[name]["CLI_CONFIG"].items():
                    if val.get("dyne"):
                        val["source"] = name
                        cli_draw[key] = val
                hub.pop.dicts.update(raw[cli]["CLI_CONFIG"], cli_draw)
    raw = hub.config.inject.add(cli, raw)
    return raw


def verify(hub, opts):
    """
    Verify that the environment and all named directories in the
    configuration exist
    """
    for imp in opts:
        for key in opts[imp]:
            if key == "root_dir":
                continue
            if key == "config_dir":
                continue
            if key.endswith("_dir"):
                if not os.path.isdir(opts[imp][key]):
                    os.makedirs(opts[imp][key])
