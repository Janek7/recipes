import configparser
import os
from typing import Dict


def get_config() -> Dict:
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.path.dirname(__file__), 'config.ini')

    config.read(ini_path)

    # Assuming the section name is 'Settings' in the INI file
    settings = config['Settings']
    
    result = {
        'api_key': settings.get('huggingface_access_token')
    }

    return result

config = get_config()


if __name__ == '__main__':
    print(get_config())
