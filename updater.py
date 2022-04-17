from replication.constants import STATE_INITIAL


class SessionData():
    """ A structure to share easily the current session data across the addon
        modules.
        This object will completely replace the Singleton lying in replication
        interface module.  
    """

    def __init__(self):
        self.repository = None  # The current repository
        self.remote = None  # The active remote
        self.server = None
        self.applied_updates = []

    @property
    def state(self):
        if self.remote is None:
            return STATE_INITIAL
        else:
            return self.remote.connection_status

    def clear(self):
        self.remote = None
        self.repository = None
        self.server = None
        self.applied_updates = []


session = SessionData()
