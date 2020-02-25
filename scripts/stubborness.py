import numpy as np
false = False
true = True

dump = [
        {
         "nodes": [
                    {"choice": false, "preference": false, "id": 3},
                    {"choice": false, "preference": false, "id": 1},
                    {"choice": false, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": false, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.2,
         "time": 1567771273.535299,
         "choice": "start_of_round"
        },
        {
         "nodes": [
                    {"choice": false, "preference": false, "id": 3},
                    {"choice": false, "preference": false, "id": 1},
                    {"choice": false, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.4,
         "time": 1567771297.495562,
         "choice": {"id": 4, "value": true, "subjective_time": 22}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": false, "preference": false, "id": 1},
                    {"choice": false, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.6,
         "time": 1567771301.056135,
         "choice": {"id": 3, "value": true, "subjective_time": 25}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": false, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771306.030917,
         "choice": {"id": 1, "value": true, "subjective_time": 30}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 1.0,
         "time": 1567771328.0669193,
         "choice": {"id": 5, "value": true, "subjective_time": 53}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": false, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771380.907936,
         "choice": {"id": 2, "value": false, "subjective_time": 105}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 1.0,
         "time": 1567771382.3306215,
         "choice": {"id": 2, "value": true, "subjective_time": 106}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": false, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771386.9837487,
         "choice": {"id": 4, "value": false, "subjective_time": 111}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 1.0,
         "time": 1567771387.4277499,
         "choice": {"id": 4, "value": true, "subjective_time": 112}
        },
        {
         "nodes": [
                    {"choice": false, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771389.222851,
         "choice": {"id": 3, "value": false, "subjective_time": 113}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
          "minority_ratio": 1.0,
          "time": 1567771389.5938647,
          "choice": {"id": 3, "value": true, "subjective_time": 113}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": false, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771391.3761487,
         "choice": {"id": 2, "value": false, "subjective_time": 115}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 1.0,
         "time": 1567771391.7543373,
         "choice": {"id": 2, "value": true, "subjective_time": 115}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": false, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 0.8,
         "time": 1567771393.5863657,
         "choice": {"id": 1, "value": false, "subjective_time": 117}
        },
        {
         "nodes": [
                    {"choice": true, "preference": false, "id": 3},
                    {"choice": true, "preference": false, "id": 1},
                    {"choice": true, "preference": false, "id": 5},
                    {"choice": true, "preference": true, "id": 2},
                    {"choice": true, "preference": false, "id": 4}
                  ],
         "minority_ratio": 1.0,
         "time": 1567771393.9870524,
         "choice": {"id": 1, "value": true, "subjective_time": 118}
        }
       ]

stubborn = {}
start_time = dump[0]['time']
final_time = dump[len(dump)-1]['time']
print('tot_time', final_time - start_time)
# ids = dump[1]['nodes'][0].keys()
for i in range(1, len(dump)): # for hver gang nogen har trykket på en knap...
    print('\n')
    time = dump[i]['time']
    id = dump[i]["choice"]['id']
    choice = dump[i]["choice"]['value']
    preference = next(item for item in dump[i]['nodes'] if item["id"] == id)['preference']
    (last_time, stubborness, c) = stubborn.get(id, (start_time,0,0)) # gem det i ordbogen
    c += 1
    if choice == preference:
        last_time = time
    else:
        # if part of minority in ego-network:
        stubborness += time - last_time

    print(id, choice, preference) # print hvem det er...
    print(dump[i]['time'] - start_time)
    stubborn[id] = (last_time, stubborness, c)
print(stubborn)
