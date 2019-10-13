dockerfile = {
    'nodejs': 'app/docker/nodejs.Dockerfile',
    'python': 'app/docker/python.Dockerfile'
}


def get_dockerfile(type):
    with open(dockerfile.get(type, None)) as f:
        return f.read()
