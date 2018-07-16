class Container:
    def __init__(self, ip = None, docker_list = None):
        self.__ip = ip
        self.__docker_list = docker_list

    def getContainerName(self):
        return self.__name

    def setIp(self, ip):
        self.__ip = ip

    def setDockerList(self, docker_list):
        self.__docker_list = docker_list

    def getDockerList(self):
        return self.__docker_list