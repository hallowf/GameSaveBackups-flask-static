from steam import SteamID
from steam import SteamClient
from steam.enums.emsg import EMsg

def convert_id(user_id):
    uid = SteamID(user_id)
    converted_ID = uid.as_steam3
    first_trim = converted_ID.replace("[U:1:","")
    trimmed_id = first_trim.replace("]","")
    print (trimmed_id)
    return trimmed_id
