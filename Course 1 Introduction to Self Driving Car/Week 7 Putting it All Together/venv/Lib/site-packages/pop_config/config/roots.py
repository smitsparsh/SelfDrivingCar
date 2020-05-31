"""
Used to take care of the options that end in `_dir`. The assumption is that
`_dir` options need to be treated differently. They need to verified to exist
and they need to be rooted based on the user, root option etc.
"""
# Import python libs
import os


def apply(hub, ret, raw, cli):
    """
    Take the initial defaults and apply the roots system to set the values
    to be either root or in user dotfiles
    """
    default_root = raw.get(cli, {}).get("CONFIG", {}).get("root_dir")
    root_dir = ret.get(cli, {}).get("root_dir")
    os_root = os.path.abspath(os.sep)
    root = os_root
    change = False
    non_priv = False
    if hasattr(os, "geteuid"):
        if not os.geteuid() == 0:
            change = True
            non_priv = True
    if root_dir and root_dir != default_root:
        root = root_dir
        change = True
    if not root.endswith(os.sep):
        root = f"{root}{os.sep}"
    if change:
        for imp in ret:
            for key, val in ret[imp].items():
                if key == "root_dir":
                    continue
                if key.endswith("_dir"):
                    if non_priv:
                        root = os.path.join(os.environ["HOME"], f".{imp}{os.sep}")
                    if imp in val:
                        typename = os.path.basename(
                            os.path.dirname(val[: val.index(imp)])
                        )
                        a_len = len(imp) + 1
                        tgt = os.path.join(
                            root, typename, val[val.index(imp) + a_len :]
                        )
                        ret[imp][key] = tgt
                    else:
                        ret[imp][key] = ret[imp][key].replace(os_root, root, 1)
    return ret
