import json
import requests
import trm_token
from trm_token import aciat001_trm_token

worker_update_dict = {
    "total": 41,
    "updated": 37,
    "inProgress": 0,
    "failed": 4,
    "tasks": [
        {
            "taskId": "6275568e-542a-4268-a556-45d535a1a141",
            "currentVersion": "",
            "tenantName": "mc105",
            "status": "FAILED",
            "retryable": True,
            "errorDescription": "prepareTenantForSoftwareUpdate: Update cannot be started for Tenant: mc105 MasterTaskId: 950223 for Version: chaos_2021-12-12 22:45:16.008148 as Partition in Invalid State"
        },
        {
            "taskId": "c904a89c-43a0-4542-8db8-0f7125775ca5",
            "currentVersion": "",
            "tenantName": "isuitestresstests",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "ae392a52-e49d-4b27-9798-da6c4dc78b79",
            "currentVersion": "",
            "tenantName": "mc101",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "1d5a9f1b-2f96-4e2d-8ddc-50ab6ccedd7d",
            "currentVersion": "",
            "tenantName": "createvehicleapp",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "9823e812-da8d-45cc-9623-9b420a5dfbed",
            "currentVersion": "",
            "tenantName": "mc102",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "2c46f89f-a65c-44dc-b561-ce389cd77e27",
            "currentVersion": "",
            "tenantName": "mc103",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "7f1414ad-fcff-4d12-8a29-afac6f1d22cd",
            "currentVersion": "",
            "tenantName": "iat-oidp",
            "status": "FAILED",
            "retryable": True,
            "errorDescription": "The task timeout has been reached"
        },
        {
            "taskId": "16801d55-2113-4f0b-8fbb-aeeaa2e13f39",
            "currentVersion": "",
            "tenantName": "prismisuite",
            "status": "FAILED",
            "retryable": True,
            "errorDescription": "The task timeout has been reached"
        },
        {
            "taskId": "5d123dfb-6bf3-4a5c-9ff3-26fcc2619f35",
            "currentVersion": "",
            "tenantName": "unboxing",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "24b87e21-9719-4358-bef3-1864391eaf49",
            "currentVersion": "",
            "tenantName": "mctms",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "26befad5-04bf-4b73-8e0b-7550e342ee83",
            "currentVersion": "",
            "tenantName": "iat-aws-h",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "da6131b8-40dc-47e8-a591-216daaa0470a",
            "currentVersion": "",
            "tenantName": "oppdev",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "3a538a37-ca90-4291-953a-004d5db76396",
            "currentVersion": "",
            "tenantName": "cig-dev-gov-cpi-prod",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "364c02ed-c603-4870-abf7-8802df3e0c80",
            "currentVersion": "",
            "tenantName": "pet-multiaz-01",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "eab120b5-ccf5-4abe-9b44-e062fad9fa61",
            "currentVersion": "",
            "tenantName": "isuitemeteringtests",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "89676d70-8a8f-46a5-a3ef-3106eb642afb",
            "currentVersion": "",
            "tenantName": "recovery3",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "21a49252-926f-46e1-a8db-41a714b248c5",
            "currentVersion": "",
            "tenantName": "petaws",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "6f5785e7-7023-48cf-ab4e-be75a0b58b30",
            "currentVersion": "",
            "tenantName": "iat-custom-domain-ui",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "921c15a5-2585-494f-9f78-234e27d51950",
            "currentVersion": "",
            "tenantName": "pimission",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "8947c93c-e76f-4913-8977-4c8edbbc55f1",
            "currentVersion": "",
            "tenantName": "atpmperf",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "937aa145-94ac-4641-9dd5-80469f124f2f",
            "currentVersion": "",
            "tenantName": "atpmdev",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "57861c8f-97fc-455b-8b70-aeaad2e79656",
            "currentVersion": "",
            "tenantName": "mc115",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "cbf69a56-026e-4818-b10a-87b9771ff84c",
            "currentVersion": "",
            "tenantName": "pet-multiaz-02",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "0dde1c68-4816-4fde-b4c0-fac371b7d2e1",
            "currentVersion": "",
            "tenantName": "ibsona",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "7322fbd7-3ecc-4bc6-941f-92afdb29aa70",
            "currentVersion": "",
            "tenantName": "susexpeu10",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "dfe52fd4-aae8-4d5f-9117-a9b1e0100524",
            "currentVersion": "",
            "tenantName": "cts-aws-h",
            "status": "FAILED",
            "retryable": True,
            "errorDescription": "The task timeout has been reached"
        },
        {
            "taskId": "fbee39e2-6320-4ce0-94f0-79344fe1dfd3",
            "currentVersion": "",
            "tenantName": "awsrit02",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "c03b26c0-9a91-4567-b43d-00ba607514af",
            "currentVersion": "",
            "tenantName": "cig-dev-gov-cpi-test",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "acdea8e9-675b-4250-9866-b856910b1ff2",
            "currentVersion": "",
            "tenantName": "ilmdev",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "0fa186c3-0b9e-41a3-a6a8-aad8de9485bd",
            "currentVersion": "",
            "tenantName": "fsmcpi",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "0f336f4e-a8b7-4c8c-bf7c-d49ba55f08d0",
            "currentVersion": "",
            "tenantName": "spa-lcap-playground",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "aef2a9af-f8d3-4df9-b3e6-32315223f861",
            "currentVersion": "",
            "tenantName": "tainternal1",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "c022d957-3bec-4e2e-bcba-52283781f3ba",
            "currentVersion": "",
            "tenantName": "rollback61817",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "02a70274-6504-405e-8931-4cb6358168b5",
            "currentVersion": "",
            "tenantName": "saptcancp",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "d2085b11-f884-49df-b4d2-3ede4f18f727",
            "currentVersion": "",
            "tenantName": "aws-db-failover",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "f0bf5d8c-2e9c-497d-b03f-486422934a2e",
            "currentVersion": "",
            "tenantName": "awsfreemiumtest",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "7126f3ef-c789-4fcc-92e1-e5966e783977",
            "currentVersion": "",
            "tenantName": "awsiat61314",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "38eed6d4-401c-4d44-9e69-749674fdb47a",
            "currentVersion": "",
            "tenantName": "awspv2009",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "c1bb23a7-4665-4448-95a0-fb3f04688689",
            "currentVersion": "",
            "tenantName": "awsiatmaz",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "a0e7fa8e-8b3d-447e-974e-ada607a05f05",
            "currentVersion": "",
            "tenantName": "iag-cf-dev01",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        },
        {
            "taskId": "37284dd5-c351-4dd6-91ee-a3ae37c7d432",
            "currentVersion": "",
            "tenantName": "recovery6",
            "status": "SUCCESS",
            "retryable": True,
            "errorDescription": ""
        }
    ]
}


def failed_tasks(worker_update_file):
    task_sub_dict = {}
    subtask_dict = {}
    # failed_tasks = []
    for task in range(0, len(worker_update_file["tasks"])):
        if (worker_update_file["tasks"][task]["status"]) == "FAILED":
            taskId = worker_update_file["tasks"][task]["taskId"]
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
            # print(f"max retry count is {max(retrycount_list)}")

            for subtask in range(0, len(response_in_dict)):
                # print("test")
                if (response_in_dict[subtask]["retryCount"]) == max(retrycount_list):
                    # print(response_in_dict[subtask])
                    # subtask_affected = json.dumps(response_in_dict[subtask], indent=4)
                    subtask_affected = response_in_dict[subtask]
                    # print(subtask_affected)
                    subtask_dict[subtask] = subtask_affected
                    # subtask_dict[taskId] = subtask_affected
                    subtask_id = subtask_dict[subtask]["id"]
                    # print(taskId, subtask_id)
                    # task_sub_dict[taskId] = subtask_id
                    task_sub_dict[taskId] = subtask_affected
                    # print(f"subtask affected is - \n {subtask_affected}")
    # print(subtask_dict)
    print("\n")
    print(json.dumps(task_sub_dict, indent=4))
    return task_sub_dict


def main():
    failed_tasks(worker_update_file=worker_update_dict)


if __name__ == "__main__":
    main()
