station_dict = {
    '石家庄': 'SJP',
    '北京西': 'BXP',
    '高平东': 'GVF',
    '阜新': 'FOT',
    '北京朝阳': 'IFP'
}


def get_station_code(station_name):
    for station_name_, station_code_ in station_dict.items():
        if station_name_ == station_name:
            return station_code_
    return ''
