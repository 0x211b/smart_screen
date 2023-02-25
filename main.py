# PYTHON SMART MIRROR
# AUTHOR:   0x211b
# 2/22/2023

# https://github.com/0x211b/smart_screen/blob/master/README.md

import json



# Variable declarations

top_list = []
mid_list = []
btm_list = []
header = ""
footer = ""

modules = []

def get_config():

    try:                                                                    # try successful operation below
            json_file = open("config.json", "r")                            # open config.json file
            global config_dict
            config_dict = json.load(json_file)                              # load json into dictionary
            json_file.close()                                               # close file

    except:                                                             # if operation fails, print message and quit
            print("\n**  An error occurred in loading 'config.json'  **\nPlease verify proper formatting of data in the file.\n")
            quit()                                                          # do not proceed




if __name__ == '__main__':
    get_config()                                        # load config JSON file into dictionary

#   ***   GET POSITIONS OF MODULES   ***
#   get list of module names for each row (1 for header and footer, list for top,mid and bottom)
    modules = config_dict["module"]
    for module in modules:
        if "top" in module["position"]:
            top_list.append(module)                         # add name of top row modules
        elif "mid" in module["position"]:
            mid_list.append(module)                         # add name of mid row modules
        elif "bottom" in module["position"]:
            btm_list.append(module)                         # add name of bottom row modules
        elif "header" in module["position"]:
            header = module                                 # add name of header module
        elif "footer" in module["position"]:
            footer = module                                 # add name of footer module

#   Error check for more than 3 modules per row
    if len(top_list) > 3:
        print("\nError!  More than three top row modules.\n")
        quit()                                                          # quit with error message
    elif len(mid_list) > 3:
        print("\nError!  More than three middle row modules.\n")
        quit()                                                          # quit with error message
    elif len(btm_list) > 3:
        print("\nError!  More than bottom top row modules.\n")
        quit()                                                          # quit with error message

    print(header)
    print(top_list)
    print(mid_list)
    print(btm_list)
    print(footer)
