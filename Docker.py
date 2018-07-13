import DockerInfo


def createDocker(docker_name, docker_ip, docker_status):
    return Docker(docker_name, DockerInfo(docker_ip, docker_status))


class Docker:
    def __init__(self, dname, docker_info):
        self.dname = dname
        self.docker_info = docker_info

    #
    @property
    def GetDockerName(self):
        return self.dname

    # noinspection PyPropertyDefinition
    @property
    def SetDockerName(self, dname):
        self.dname = dname

    # noinspection PyPropertyDefinition
    @property
    def DeleteDockerName(self):
        del self.dname
