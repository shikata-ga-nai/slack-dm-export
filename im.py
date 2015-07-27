from slacker import Slacker
from datetime import timedelta, datetime
from time import mktime
import sys, os

slack = Slacker('API_KEY_GOES_HERE')

def daterangetimestamp(start_range_date, end_range_date):
    for n in range(int((end_range_date - start_range_date).days)):
        current_date = start_range_date + timedelta(n)
        current_date_time = datetime.combine(current_date, datetime.min.time())
        yield mktime(current_date_time.timetuple())+1e-6*current_date_time.microsecond

def dm_export():
    im_list = slack.im.list().body['ims']
    for i in range(0, len(im_list)):
            current_user = im_list[i]['user']
            current_username = slack.users.info(current_user).body['user']['name']
            log_file = open(current_username+'.json', 'a')
            print('[+] ' + current_username)
            for single_date_timestamp in daterangetimestamp(start_date, end_date):
                history = slack.im.history(im_list[i]['id'], count=1000, oldest=single_date_timestamp,
                                          latest=single_date_timestamp+86400.0).body['messages']
                for item in history:
                    log_file.write("%s\n" % item)
            log_file.close()
            if os.stat(current_username+'.json').st_size == 0:
                os.remove(current_username+'.json')


def general_export():
    file = open('general.json', 'a')
    for single_date_timestamp in daterangetimestamp(start_date, end_date):
        response = slack.channels.history('C04JFRF4V', count=1000, oldest=single_date_timestamp,
                                          latest=single_date_timestamp+86400.0)
        history = response.body['messages']
        for item in history:
            file.write("%s\n" % item)
    file.close()



def private_groups_export():
    groups_list = slack.groups.list().body['groups']
    for i in range(0, len(groups_list)):
        current_group_id = groups_list[i]['id']
        current_group_name = slack.groups.info(current_group_id).body['group']['name']
        log_file = open(current_group_name+'.json', 'a')
        print('[+] ' + current_group_name)
        for single_date_timestamp in daterangetimestamp(start_date, end_date):
            response = slack.groups.history(current_group_id, count=1000, oldest=single_date_timestamp,
                                          latest=single_date_timestamp+86400.0)
            history = response.body['messages']
            for item in history:
                log_file.write("%s\n" % item)
        log_file.close()
        if os.stat(current_group_name+'.json').st_size == 0:
            os.remove(current_group_name+'.json')




start = str(sys.argv[1])
end = str(sys.argv[2])

start_date = datetime.strptime(start, "%Y.%m.%d")
end_date = datetime.strptime(end, "%Y.%m.%d")

os.system('clear')
print('========================================================================')
print('[+] Start date: ' + str(start_date))
print('[+] End date: ' + str(end_date))
print('========================================================================')
print('[+] Starting direct messages export')
dm_export()
print('[+] Direct messages export finished')
print('========================================================================')
print('[+] Starting #general channel export')
general_export()
print('[+] #general channel export finished')
print('========================================================================')
print('[+] Starting private groups export')
private_groups_export()
print('[+] Private groups export finished')
print('[+] All tasks finished')
print('========================================================================')
