import docker
import random
import string
import time
import json


class DockerManager(object):
    CONTAINER_PREFIX = 'narwhal_managed_'
    TIMEOUT_LABEL = 'org.narwhal.variables.EXPIRATION_TIMESTAMP'
    OS_LIST = None

    def __init__(self):
        self.client = docker.from_env()

        try:
            with open('app/services/services.json', 'r') as os_manifest:
                self.OS_LIST = json.load(os_manifest)
        except Exception:
            pass

        self.AVAILABLE_OS_LIST = []
        for os in self.OS_LIST:
            for ver in os['subList']:
                self.AVAILABLE_OS_LIST.append(ver['imageTag'])

    def create_container(self,
                         mem,
                         cpu,
                         os_name,
                         os_timeout=time.time(),
                         open_port=None):
        if open_port is None:
            port_dict = {}
        else:
            port_dict = {'{}/tcp'.format(self.get_port(os_name.split(':')[0])): open_port}

        container_name = self.generate_container_name()
        try:
            self.client.containers.run(
                image=os_name,
                cpu_period=100000,
                cpu_quota=int('%s0000' % cpu),
                mem_limit='%sm' % mem,
                name=container_name,
                hostname=container_name,
                ports=port_dict,
                restart_policy={'Name': 'always'},
                labels={self.TIMEOUT_LABEL: str.format('{:.0f}', os_timeout)},
                tty=True,
                detach=True,
            )
        except Exception as e:
            print(e)
        else:
            return container_name

    def get_container_ports(self, container_name):
        try:
            ports = self.client.containers.get(
                container_name).attrs['NetworkSettings']['Ports']
            return {
                port: mapped_ports[0]['HostPort']
                if mapped_ports is not None else None
                for port, mapped_ports in ports.items()
            }
        except Exception:
            return None

    def remove_timeout_containers(self):
        for container in self.client.containers.list():
            if container.name.startswith(self.CONTAINER_PREFIX):
                timeout = container.labels.get(self.TIMEOUT_LABEL)
                if timeout is not None and float(timeout) < time.time():
                    self.rm_container(container.name)

    def rm_container(self, container_name) -> bool:
        try:
            container = self.client.containers.get(container_name)
            if container.name.startswith(self.CONTAINER_PREFIX):
                container.remove(force=True)
            return True
        except docker.errors.NotFound:
            return False

    def is_os_available(self, image_tag=None) -> bool:
        return image_tag is not None and image_tag in self.AVAILABLE_OS_LIST

    def get_port(self, image):
        for OS in self.OS_LIST:
            if OS['value'] == image:
                return OS['port']

    def generate_container_name(self) -> str:
        return self.CONTAINER_PREFIX + ''.join(
            random.sample(string.ascii_lowercase + string.digits, 16))


if __name__ == '__main__':
    test = DockerManager()
    container_name = test.create_container('512', 1,
                                              'instantbox/ubuntu:latest',
                                           time.time())
    test.get_container_ports(container_name)
    test.remove_timeout_containers()
    test.rm_container(container_name)