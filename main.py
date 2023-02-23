# PYTHON SMART MIRROR
# AUTHOR:   0x211b
# 2/22/2023

# https://github.com/0x211b/smart_screen/blob/master/README.md

import json








def get_config():

    try:                                                                # try successful operation below
            json_file = open("config.json", "r")                            # open config.json file
            global config_dict
            config_dict = json.load(json_file)                              # load json into dictionary
            json_file.close()                                               # close file

    except:                                                             # if operation fails, print message and quit
            print("\n**  An error occurred in loading 'config.json'  **\nPlease verify proper formatting of data in the file.\n")
            quit()                                                          # do not proceed




if __name__ == '__main__':
    get_config()
    if "footer" in config_dict:
        print("FOOTER")
