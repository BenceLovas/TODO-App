
def query_to_dict(data, label_list):
    data_dict = {}
    for item in data:
        temp_dict = {}
        for key, value in zip(label_list, item[1:]):
            temp_dict[key] = value
        data_dict[item[0]] = temp_dict
    return data_dict


def format_time(date):
    format_str = '%Y  /  %b / %-d - %H:%M'
    return date.strftime(format_str)


def format_time_in_dict(dictionary, submission_time='submission_time'):
    for key in dictionary.keys():
        dictionary[key][submission_time] = format_time(dictionary[key][submission_time])
