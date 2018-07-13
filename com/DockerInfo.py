class DockerInfo:
    def __init__(self, dip, dstatus):
        self.ip = dip
        self.status = dstatus

    def getDockerInfoIp(self):
        return self.ip

    def setDockerInfoIp(self, dip):
        self.ip = dip

    def getDockerInfoStatus(self):
        return self.status

    def setDockerInfoStatus(self, dstatus):
        self.status = dstatus
