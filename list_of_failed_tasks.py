import json

import requests

import trm_token
from trm_token import aciat001_trm_token


def list_of_failed_tasks(worker_update_file):
    with open(worker_update_file) as datafile:
        worker_update_status = json.loads(datafile.read())
        # print(worker_update_status)
        # print(type(worker_update_status))
        failed_tasks = []
        for task in range(0, len(worker_update_status["tasks"])):
            if (worker_update_status["tasks"][task]["status"]) == "FAILED":
                failed_tasks.append((worker_update_status["tasks"][task]["taskId"]))
        print(failed_tasks)
        return failed_tasks


# print(list_of_failed_tasks(worker_update_file="worker_update.json"))
# list_of_failed_tasks(worker_update_file="worker_update.json")

for taskId in list_of_failed_tasks("worker_update.json"):
    url = f"https://it-aciat001-trm.cfapps.sap.hana.ondemand.com/api/trm/v1/tasks/{taskId}/subtasks"

    # print(url)

    payload = {}
    headers = {
        'Authorization': f'Bearer {trm_token.aciat001_trm_token()}'
    }

    subtasks = requests.request("GET", url, headers=headers, data=payload)
    response_in_dict = json.loads(subtasks.text)

    # print(json.dumps(response_in_dict, indent=4))

    retrycount_list = []
    for subtask in range(0, len(response_in_dict)):
        list_value = int((response_in_dict[subtask]["retryCount"]))
        retrycount_list.append(list_value)
    print(f"max retry count is {max(retrycount_list)}")

    for subtask in range(0, len(response_in_dict)):
        # print("test")
        if (response_in_dict[subtask]["retryCount"]) == max(retrycount_list):
            # print(response_in_dict[subtask])
            subtask_affected = json.dumps(response_in_dict[subtask], indent=4)
    print(f"subtask affected is - \n {subtask_affected}")
