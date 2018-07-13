from flask import Flask, render_template

import Docker
import Container
import DockerInfo
app = Flask(__name__)


@app.route('/')
def hello_world():

    global container_instance
    dict_container = {}

    for x in range(0, 1):
        container_name = raw_input("Enter the containername : ")
        docker_list = []
        for y in range(0, 2):
            docker_list.append(Docker.createDocker(raw_input("Enter the dockername : "), raw_input("Enter the dockerip : "),
                                            raw_input("Enter the dockerstatus : ")))
        container_instance = Container()
    dict_container[container_instance.cname] = container_instance


if __name__ == "__main__":
    app.run(debug=True)
