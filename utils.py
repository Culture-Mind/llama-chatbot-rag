import os
import yaml

def get_apikey():
    script_dir = "./"
    file_path = os.path.join(script_dir, "apikeys.yml")

    with open(file_path, 'r') as yamlfile:
        
        loaded_yamlfile = yaml.safe_load(yamlfile)
        API_KEY = loaded_yamlfile['openai']['api_key']
    return API_KEY

if __name__ == "__main__":
    print("API_KEY", get_apikey())