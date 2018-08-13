from steam import SteamID
import time


def convert_id(user_id):
    uid = SteamID(user_id)
    if uid.is_valid():
        return str(uid.id)
    else:
        raise ValueError("The id you submitted is either incorrect or invalid")

def convert_id_from_url(the_url):
    uid = SteamID.from_url(the_url, http_timeout=20)
    wait_time = time.time() + 21
    while True:
        if time.time() < wait_time and uid == None:
            continue
        elif uid != None:
            converted_ID = uid.as_steam3
            first_trim = converted_ID.replace("[U:1:","")
            trimmed_id = first_trim.replace("]","")
            return trimmed_id
        else:
            raise ValueError("The url you provided is either incorrect or invalid")
