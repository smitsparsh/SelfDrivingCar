# Import python libs
import copy


def add(hub, cli, raw):
    """
    Inject any additional arguments onto the raw input that the config system
    wants to add, such as logging and version checking.
    """
    keys = set()
    if "CONFIG" not in raw[cli]:
        raw[cli]["CONFIG"] = {}
    # Merge in log configs
    dst = hub.log.init.conf(cli)
    keys.update(dst.keys())
    hub.pop.dicts.update(dst, raw[cli]["CONFIG"])
    raw[cli]["CONFIG"] = dst
    # Merge in Version configs
    dst = copy.deepcopy(hub.config.version.CONFIG)
    keys.update(dst.keys())
    hub.pop.dicts.update(dst, raw[cli]["CONFIG"])
    raw[cli]["CONFIG"] = dst
    # Apply the CLI_CONFIG
    for key in sorted(keys):
        if key not in raw[cli]["CLI_CONFIG"]:
            raw[cli]["CLI_CONFIG"][key] = {}
    return raw
