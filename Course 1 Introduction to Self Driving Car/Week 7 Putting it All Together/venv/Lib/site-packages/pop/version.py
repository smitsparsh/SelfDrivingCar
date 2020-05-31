# -*- coding: utf-8 -*-
def get_ver():
    """
    Gather the version number from git
    """
    import subprocess

    proc = subprocess.run(
        ["git", "describe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if not proc.returncode == 0:
        return
    v = proc.stdout.decode().strip()
    if "-" not in v:
        ret = v
    else:
        csum = v[v.rindex("-") + 1 :]
        base = v[: v.rindex("-")]
        count = base[base.rindex("-") + 1 :]
        tag = base[: base.rindex("-")]
        ret = f"{tag}.post{count}+{csum}"
    return ret


version = get_ver()
