#!/usr/bin/python3
""" python input output """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


import json
import sys


arguments = sys.argv[1:]
data_list = []
data_list.extend(arguments)
save_to_json_file(data_list, "add_item.json")
