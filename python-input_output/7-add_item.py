#!/usr/bin/python3
""" python input output """
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


arguments = sys.argv[1:]
try:
    data_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    data_list = []
data_list.extend(arguments)

save_to_json_file(data_list, "add_item.json")
