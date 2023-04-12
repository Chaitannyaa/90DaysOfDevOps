import json
import yaml

yaml_file = "DevOps-90DaysChallenge\services.yaml"
json_file = "DevOps-90DaysChallenge\created_file.json"

with open(yaml_file, 'r') as yfile:
    data = yaml.safe_load(yfile)

with open(json_file, 'w') as jfile:
    json.dump(data, jfile, indent=3)
