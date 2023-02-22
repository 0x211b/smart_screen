# PYTHON SMART MIRROR
# AUTHOR:   0x211b
# 2/22/2023

# https://github.com/0x211b/smart_screen/blob/master/README.md

import json






if __name__ == '__main__':

    json_file = open("config.json", "r")                            # open config.json file
    config_dict = json.load(json_file)                              # load json into dictionary
    json_file.close()                                               # close file

    for i in config_dict:                                           # test success of json variables
        print(i)

    print ("\n")
    print(config_dict)