import json

dict = {
    "Cloud provider": "AWS",
    "IaC tool": "terraform",
    "Config.mgmt tool": "Ansible"
}

json_file = "DevOps-90DaysChallenge\DevOps.json"

with open(json_file, "w") as f:
    json.dump(dict, f, indent = 4)