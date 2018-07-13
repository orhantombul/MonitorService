class Container:
    def __init__(self, cname, docker_list):
        self.name = cname
        self.docker_list = docker_list

    #
    @property
    def GetContainerName(self):
        return self.name

    # noinspection PyPropertyDefinition
    @property
    def SetContainerName(self, cname):
        self.name = cname

    # noinspection PyPropertyDefinition
    @property
    def DeleteContainerName(self):
        del self.name

