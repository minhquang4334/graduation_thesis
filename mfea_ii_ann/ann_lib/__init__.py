import os
import yaml
from .taskset import Taskset

BASEDIR = os.path.dirname(__file__)

def create_taskset(instance):
    config = yaml.load(open(os.path.join(BASEDIR, 'data/instances.yaml')).read())
    taskset = Taskset(config[instance])
    return taskset
