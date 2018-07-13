class DockerInfo:
    def __init__(self, dip, dstatus):
        self.ip = dip
        self.status = dstatus

    @property
    def GetDockerInfoIp(self):
        return self.ip

    # noinspection PyPropertyDefinition
    @property
    def SetDockerInfoIp(self, dip):
        self.ip = dip

    # noinspection PyPropertyDefinition
    @property
    def DeleteDockerInfoIp(self):
        del self.ip

    @property
    def GetDockerInfoStatus(self):
        return self.status

    # noinspection PyPropertyDefinition
    @property
    def SetDockerInfoStatus(self, dstatus):
        self.status = dstatus

    # noinspection PyPropertyDefinition
    @property
    def DeleteDockerInfoStatus(self):
        del self.status
