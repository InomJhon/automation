import yaml
from features.ui.step_definitions import *

data = yaml_loader("/Users/inomnematov/Desktop/automation/guru99/data/configs.yaml") 

print(data['url'])