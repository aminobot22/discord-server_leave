import requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

def get_headers(auth_token):
    return {
        'Host': 'discord.com',
        'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        
        'X-Debug-Options': 'bugReporterEnabled',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': auth_token,
        'User-Agent': user_agent_rotator.get_random_user_agent(),
        'X-Discord-Timezone': 'Asia/Calcutta',
        'X-Discord-Locale': 'en-GB',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://discord.com/app',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        
    }


def leave_guild(auth_token,guild_id):
    json_data = {
    'lurking': False,
    }
    response = requests.delete(
        f'https://discord.com/api/v9/users/@me/guilds/{guild_id}',
        headers=get_headers(auth_token),
        json=json_data,
    )
    return response.text

def get_guild_ids(auth_token):
    response = requests.get('https://discord.com/api/v9/users/@me/guilds',headers=get_headers(auth_token))
    return response

