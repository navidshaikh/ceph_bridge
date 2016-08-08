from etcdobj import EtcdObj, fields


CRITICAL = 1
ERROR = 2
WARNING = 3
RECOVERY = 4
INFO = 5

SEVERITIES = {
    CRITICAL: "CRITICAL",
    ERROR: "ERROR",
    WARNING: "WARNING",
    RECOVERY: "RECOVERY",
    INFO: "INFO"
}

STR_TO_SEVERITY = dict([(b, a) for (a, b) in SEVERITIES.items()])


def severity_str(severity):
    return SEVERITIES[severity]


def severity_from_str(severitry_str):
    return STR_TO_SEVERITY[severitry_str]


class Event(EtcdObj):
    """
    Events generated by the ceph_bridge Eventer.
    """
    __name__ = 'raw/ceph/%s/events/%s'

    id = fields.StrField("uuid")

    # Time at which event was synthesized by Eventer
    when = fields.DateTimeField("when", "%Y-%m-%dT%H:%M:%S%Z")

    severity = fields.IntField("severity")

    # Human readable message
    message = fields.StrField("message")

    # Optionally associated with a cluster
    fsid = fields.StrField("fsid")
    # Optionally associated with a server
    fqdn = fields.StrField("fqdn")
    # Optionally associated with a service type ('osd', 'mon', 'mds') (FSID must be set)
    service_type = fields.StrField("service_type")
    # Optionally associate with a particular service (service_type must be set)
    service_id = fields.StrField("service_id")


    def render(self):
        self.__name__ = self.__name__ % (self.fsid, self.id)
        return super(Event, self).render()

