def get(hub):
    """
    Retrive the dynamic dirs data for this hub, if dynamic dirs have not been
    gathered yet then gather it.
    """
    if not hub._dscan:
        hub._scan_dynamic()
    return hub._dynamic


def refresh(hub):
    """
    Refresh the dynamic dirs
    """
    hub._scan_dynamic()
