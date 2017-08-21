import datetime
import pytz

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


def format_time_in_dict(dictionary, submission_time='submission_time', elapsed_time='elapsed_time'):
    for key in dictionary.keys():
        dictionary[key][submission_time] = format_time(dictionary[key][submission_time])
        dictionary[key][elapsed_time] = td_format(dictionary[key][elapsed_time])


def elapsed_time(past_date):
    return datetime.datetime.now(pytz.utc) - past_date


def td_format(td_object):
        seconds = int(td_object.total_seconds())
        periods = [
                ('year',        60*60*24*365),
                ('month',       60*60*24*30),
                ('day',         60*60*24),
                ('hour',        60*60),
                # ('minute',      60),
                # ('second',      1)
                ]

        strings=[]
        for period_name,period_seconds in periods:
                if seconds > period_seconds:
                        period_value , seconds = divmod(seconds,period_seconds)
                        if period_value == 1:
                                strings.append("%s %s" % (period_value, period_name))
                        else:
                                strings.append("%s %ss" % (period_value, period_name))

        return ", ".join(strings) + " AGO"