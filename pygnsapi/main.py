import json
import requests
import re
import yaml





class GNS3(object):

    def __init__(self, host, port, username, password, version):

        self.host = host
        self.port = port
        self.user = username
        self.password = password
        self.version = version

        # define the base API URLs
        self.baseurl = 'http://{}:{}'.format(self.host, self.port)

    def get_appliances(self):

        url = '{baseurl}/{version}/appliances'.format(baseurl = self.baseurl, version = self.version)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print(response.status_code)
                return response
        except:
            return 'Request failed'

# project

    def get_projects(self):
        """
        Get a list of the defined projects
        :return:
        """

        url = '{baseurl}/{version}/projects'.format(baseurl=self.baseurl, version=self.version)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print(response.status_code)
                return response.json()
        except:
            return 'Request failed'

    def get_project_id(self, name):
        """
        Get a specific project based on provided name
        :param name: project name
        :return:
        """

        url = '{baseurl}/{version}/projects'.format(baseurl=self.baseurl, version=self.version)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:

                for project in response.json():

                    if project['name'] == name:
                        print(project['project_id'])
                        return project

        except:
            return 'Request failed'

    # def get_project(self):
    # def add_project(self):
    # def del_project(self):
    # def set_project(self):

# nodes

    # def get_node(self):
    def get_nodes(self, project_id):
        """
        Get a list of nodes for a configured project_id.
        :param project_id: id of project
        :return: json list of nodes.
        """

        url = '{baseurl}/{version}/appliances'.format(baseurl=self.baseurl, version=self.version)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print(response.status_code)
                return response.json()
        except:
            return 'Request failed'

    # def add_node(self):
    # def del_node(self):
    # def set_node(self):
    # def start_node(self):
    # def stop_node(self):
    # def reload_node(self):
    # def suspend_node(self):

# links

    def get_link(self, project_id):

        url = '{baseurl}/{version}/projects/{project}/links'.format(baseurl=self.baseurl, version=self.version,
                                                                    project=project_id)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print(response.status_code)
                return response.json()
        except:
            return 'Request failed'

    def add_link(self, a_node, a_port, z_node, z_port, label):
        """
        Create a new link between two defined nodes in a project.
        :param a_node:
        :param a_port:
        :param z_node:
        :param z_port:
        :param label:
        :return:
        """

        url = '{baseurl}/{version}/projects/{project}/links'.format(baseurl=self.baseurl, version=self.version,
                                                                    project=project_id)

        payload = '''{
                    "nodes": [
                        {
                            "adapter_number": 0,
                            "node_id": {a_id},
                            "port_number": {a_port}
                        },
                        {
                            "adapter_number": 0,
                            "node_id": {z_id},
                            "port_number": {z_port}
                        }
                    ]
                }'''.format(a_id = a_id, a_port = a_port, z_id = z_id, z_port = z_port)


        try:
            response = requests.post(url, data=payload, verify=False)
            if response.status_code == 200:
                print(response.status_code)
                return response.json()
        except:
            return 'Request failed'


    # def del_link(self):



# symbols

    # def get_symbol(self, id):
    # def set_symbol(self, id):


if __name__ == '__main__':

    gns_env = {'host': '10.128.16.130', 'port': 3080, 'username': 'acennami', 'password': 'blank', 'version': 'v2'}

    gns = GNS3(**gns_env)

    projects = gns.get_projects()
    appliances = gns.get_appliances()
    pid = gns.get_project_id('lab-v1')


    # print(appliances.text)
    print(pid['project_id'])









