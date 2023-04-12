import json

json_file = "DevOps-90DaysChallenge\services.json"

with open(json_file) as f:
    data = json.load(f)
    print(f'aws :{data["services"]["aws"]["name"]}')
    print(f'azure :{data["services"]["azure"]["name"]}')
    print(f'gcp :{data["services"]["gcp"]["name"]}')