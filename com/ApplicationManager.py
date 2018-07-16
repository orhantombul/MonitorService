from com.DockerInfo import DockerInfo
from com.Docker import Docker
from com.Container import Container
from com.ApplicationManager import ApplicationManager


def createDocker(docker_name, dip, dstatus):
    return Docker(docker_name, DockerInfo(dip, dstatus))


class ApplicationManager:
    __containerDictionary = {}
    __applicationManager = None

    def __getApplicationManager(self):
        if self.__applicationManager is None:
            self.__applicationManager = ApplicationManager()

        return self.__applicationManager


    def getContainer(self,container_ip):
        if container_ip is None :
            return
        return self.__containerDictionary[container_ip]

    def setContainer(self,container_ip,container):
        if container_ip is None or container is None:
            return
        self.__containerDictionary[container_ip] = container


    def __createDockerWithContainerIp(self,container_ip):
        if container_ip is None or self.__containerDictionary[container_ip] is not None:
            return

        container = Container()
        container.setIp(container_ip)
        container.setDockerList([])
        self.__containerDictionary[container_ip] = container
        return


    def addDockerByContainerIp(self, container_ip, docker):
        if container_ip is None or docker is None:
            return
        container = self.__containerDictionary[container_ip]

        if container is None:
            self.__createDockerWithContainerIp(container_ip)

        docker_list = container.getDockerList()
        docker_list.append(docker)



    def getDocker(self,container_ip,docker_ip):
        if container_ip is None or docker_ip is None:
            return

        container = self.__containerDictionary[container_ip]
        docker_list = container.getDockerList()
        for docker in docker_list:
            if docker.getDockerInfo().getDockerInfoIp()  is docker_ip:
                return docker

