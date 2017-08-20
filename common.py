
def query_to_dict(data, label_list):
    data_dict = {}
    for item in data:
        data_dict[item[0]] = {key: value for key, value in zip(label_list, item[1:])}
    return data_dict
