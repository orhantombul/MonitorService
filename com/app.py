from flask import Flask, render_template
from com.Container import Container
from com.ApplicationManager import ContainerDockerManager, createDocker

app = Flask(__name__)


@app.route('/')
def hello_world():
    global docker_list
    dict_container = {}

    for x in range(0, 1):
        container_name = (raw_input("Enter the containername : "))
        docker_list = []
        for y in range(0, 2):
            docker_list.append(createDocker(raw_input("Enter the dockername:"), raw_input("Enter the dockerip :"), raw_input("Enter the docker status :")))
        container_instance = Container(container_name, docker_list)
        container_instance.setDockerList(docker_list)
        dict_container[container_instance.name] = container_instance
    return render_template("robot.html", color=True, container_dictionary=dict_container)


if __name__ == "__main__":
    app.run(debug=True)
