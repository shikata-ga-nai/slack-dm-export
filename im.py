from slacker import Slacker
from datetime import timedelta, date, datetime
from time import mktime

slack = Slacker('API GOES HERE')

def daterangetimestamp(start_range_date, end_range_date):
    for n in range(int((end_range_date - start_range_date).days)):
        current_date = start_range_date + timedelta(n)
        current_date_time = datetime.combine(current_date, datetime.min.time())
        yield mktime(current_date_time.timetuple())+1e-6*current_date_time.microsecond

start_date = date(2015, 4, 26)
end_date = date(2015, 7, 28)

im_list = slack.im.list().body['ims']
number_of_users = len(im_list)

for i in range(0, len(im_list)):
        current_user = im_list[i]['user']
        current_username = slack.users.info(current_user).body['user']['name']
        log_file = open(current_username+'.json', 'a')
        print(current_username)
        for single_date_timestamp in daterangetimestamp(start_date, end_date):
            history = slack.im.history(im_list[i]['id'], count=1000, oldest=single_date_timestamp,
                                      latest=single_date_timestamp+86400.0).body['messages']
            for item in history:
                log_file.write("%s\n" % item)
        log_file.close()

