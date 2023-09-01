import configparser
import os

def get_credentials():
    config = configparser.ConfigParser()
    
    # Define the path to the settings folder and the config.ini file
    settings_folder = os.path.join(os.getcwd(), 'settings')
    config_file = os.path.join(settings_folder, 'config.ini')
    
    # Create the settings folder if it doesn't exist
    if not os.path.exists(settings_folder):
        os.makedirs(settings_folder)
    
    # Check if the config.ini file exists and has the necessary information
    if not os.path.exists(config_file) or not config.read(config_file) or not config.has_section('Credentials'):
        account = input("輸入 account : ")
        password = input("輸入 password : ")
        
        # Save to config.ini
        config.add_section('Credentials')
        config.set('Credentials', 'account', account)
        config.set('Credentials', 'password', password)
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        account = config.get('Credentials', 'account')
        password = config.get('Credentials', 'password')

    return account, password

