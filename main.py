from util import *
import time
SLEEP_TIME=10 # minimum
AUTH_TOKEN="auth token from inspect"
WHITE_LIST_IDS=[1,2,3]
guil_res=guild_list=get_guild_ids(AUTH_TOKEN) #Provide a list of all the servers that your account is in.
if guil_res.status_code==200:

    for guild_dict in guil_res.json():
        guild_id=guild_dict["id"]
        if guild_id not in WHITE_LIST_IDS:
            print(guild_id)
            time.sleep(SLEEP_TIME)
            print(leave_guild(AUTH_TOKEN,guild_id)) #print empty string if working
