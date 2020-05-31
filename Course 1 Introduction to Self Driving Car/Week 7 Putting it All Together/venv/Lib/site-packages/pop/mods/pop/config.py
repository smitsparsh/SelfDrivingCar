def load(hub, sources, cli=None, dyne_name=None, loader="yaml", parse_cli=True):
    """
    Use the pop-config system to load up a fresh configuration for this project
    from the included conf.py file.
    """
    hub.pop.sub.add(dyne_name="config")
    hub.config.integrate.load(sources, cli, dyne_name, loader, parse_cli)
