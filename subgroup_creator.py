from api_helpers.super_func import *
from pprint import pprint
import argparse


# This script will take a filepath to a keyfile and will also take the ID of a device group to create subgroups for Kerry's Dashboards

# #########################
# # CLI ARGUMENT HANDLING #
# #########################

# parser=argparse.ArgumentParser()

# parser.add_argument('-file', help='Path to file containing API credentials')
# parser.add_argument('-id', help='The ID of a LogicMonitor device group to create dynamic subgroups for')

# args = parser.parse_args()

# ###################
# # PARSE API CREDS #
# ###################

# key_file_path = args.file
# file = open(key_file_path, 'r')
# file_text = file.read()

# key_file_json = json.loads(file_text)
# lm_id = key_file_json['lm_id']
# lm_key = key_file_json['lm_key']
# lm_company = key_file_json['lm_company']

# group_id = args.id

# THE ABOVE IS INTENDED FOR RELEASE
# THE BELOW IS HARDCODED FOR TESTING

lm_id      = 'wv2NAH8BGTqz7p2YEHHV'
lm_key     = 'J}HH5=_Kc]SW53jd=kEc8t3[6P!L!E$ZgX8ui2x('
lm_company = 'ianbloom'

group_id      = 39

SUBGROUP_POSTER(lm_id, lm_key, lm_company, group_id)