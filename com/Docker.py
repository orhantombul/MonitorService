from com.DockerInfo import DockerInfo


def createDocker(docker_name, dip, dstatus):
    return Docker(docker_name, DockerInfo(dip, dstatus))


class Docker:
    def __init__(self, dname, docker_info):
        self.dname = dname
        self.docker_info = docker_info

    def getDockerName(self):
        return self.dname

    def setDockerName(self, dname):
        self.dname = dname
