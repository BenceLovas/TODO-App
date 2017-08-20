
def query_to_dict(data, label_list):
    data_dict = {}
    for item in data:
        temp_dict = {}
        for key, value in zip(label_list, item[1:]):
            if key == 'submission_time':
                value = format_time(value)
                temp_dict[key] = value
            else:
                temp_dict[key] = value
        data_dict[item[0]] = temp_dict
    return data_dict


def format_time(date):
    format_str = '%b/%-d/%Y  %H:%M'
    return date.strftime(format_str)
