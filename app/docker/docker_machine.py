from app import docker_machine
import docker


class DockerMachine:

    BASE_CPU = 0.5
    BASE_MEMORY = 512
    BASE_DISK_SIZE = 5000

    @staticmethod
    def create(self, username, cpu=BASE_CPU, memory=BASE_MEMORY, disk_size=BASE_DISK_SIZE):
        cpu = ['--virtualbox-cpu-count', cpu]
        memory = ['--virtualbox-memory', memory]
        disk_size = ['--virtualbox-disk-size', disk_size]
        err = docker_machine.create(username, xarg=cpu+memory+disk_size)
        if err:
            print(err)
            raise