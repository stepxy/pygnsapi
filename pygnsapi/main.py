import json
import requests
import re
import yaml
import pprint as pp

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
                        return project

        except:
            return 'Request failed'

    # def get_project(self):
    # def add_project(self):
    # def del_project(self):
    # def set_project(self):

# nodes

    # def get_node_id(self):



    def get_nodes(self, project_id):
        """
        Get a list of nodes for a configured project_id.
        :param project_id: id of project
        :return: json list of nodes.
        """

        url = '{baseurl}/{version}/projects/{project_id}/nodes'.format(baseurl=self.baseurl, version=self.version, project_id = project_id)

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
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
                return response.json()
        except:
            return 'Request failed'


    # def del_link(self):



# symbols

    # def get_symbol(self, id):
    # def set_symbol(self, id):


# utilities

    def get_port_by_name(self, project, node, port):
        """
        Get port details for a specific node.

        :param project: project_id
        :param node: name (hostname) of the node to query
        :param port: name (shortname) of the node to query
        :return: dict({'node': node['name'], 'node_id': node['node_id'],
                                   'adapter_number': port['adapter_number'], 'port_number': port['port_number'],
                                   'port_name': port['name'], 'port_short_name': port['short_name']})
        """
        project_id = project
        node_name = node
        port_name = port

        nodes = self.get_nodes(project_id)

        #find the nodes in the list of nodes, then find the port in the list of ports - based on the port shortname.
        for node in nodes:
            if node['name'] == node_name:
                for port in node['ports']:
                    if port['short_name'] == port_name:
                        portval = {'node': node['name'], 'node_id': node['node_id'],
                                   'adapter_number': port['adapter_number'], 'port_number': port['port_number'],
                                   'port_name': port['name'], 'port_short_name': port['short_name']}
                        return portval
            else:
                print('Node not found!')
                return None



if __name__ == '__main__':

    gns_env = {'host': '10.128.16.130', 'port': 3080, 'username': 'acennami', 'password': 'blank', 'version': 'v2'}

    gns = GNS3(**gns_env)

    projects = gns.get_projects()
    appliances = gns.get_appliances()
    pid = gns.get_project_id('lab-v1')
    # print(pid)


    project_id = pid['project_id']
    # node_1_id =

    # print(appliances.text)
    # print(pid['project_id'])

    project_nodes = gns.get_nodes(project_id)
    # pp.pprint(project_nodes)

    port_a = gns.get_port_by_name(project_id, 'n9k-spine-1', 'e1/1')
    print(port_a)










