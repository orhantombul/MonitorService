class Container:
    def __init__(self, cname, docker_list):
        self.name = cname
        self.docker_list = docker_list

    def getContainerName(self):
        return self.name

    def setName(self, cname):
        self.name = cname

    def setDockerList(self, docker_list):
        self.docker_list = docker_list