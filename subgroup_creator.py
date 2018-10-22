from api_helpers.super_func import *
from api_helpers.lm_api import *
from dash_obtainer import *
from pprint import pprint
import argparse
import os
import sys

# This script will take a filepath to a keyfile and will also take the ID of a device group to create subgroups for Kerry's Dashboards

#########################
# CLI ARGUMENT HANDLING #
#########################

parser = argparse.ArgumentParser()

parser.add_argument('-file', help='Path to file containing API credentials')
parser.add_argument('-group', help='The ID of a LogicMonitor device group to create dynamic subgroups and dashboards for')
parser.add_argument('-dash', help='The ID of a LogicMonitor dashboard to extract')

args = parser.parse_args()
args_dict = vars(args)

###################
# PARSE API CREDS #
###################

key_file_path = args_dict['file']
file = open(key_file_path, 'r')
file_text = file.read()

key_file_json = json.loads(file_text)
lm_id = key_file_json['lm_id']
lm_key = key_file_json['lm_key']
lm_company = key_file_json['lm_company']

# lm_id = "wv2NAH8BGTqz7p2YEHHV"
# lm_key = "J}HH5=_Kc]SW53jd=kEc8t3[6P!L!E$ZgX8ui2x("
# lm_company = "ianbloom"

# args_dict = {}
# args_dict['group'] = 42

cwd = os.getcwd()

if(args_dict['group'] != None):
    group_id = args_dict['group']

    # get_dict will consist of a name and a device group full path
    get_dict = SUBGROUP_GETTER(lm_id, lm_key, lm_company, group_id)
    # we supply SUBGROUP_POSTER with the device group full path for applies to logic
    SUBGROUP_POSTER(lm_id, lm_key, lm_company, group_id, get_dict['path'])
    # post dashboard group with default device group token
    dash_response = DASH_GROUP_POSTER(
        lm_id, lm_key, lm_company, get_dict['name'], get_dict['path'])
    dash_json = json.loads(dash_response['body'])
    pprint(dash_json)
    dash_group_id = dash_json['id']

    file_array = os.listdir('./dashboards')

    for file in file_array:
        # Apparently I need to test if this is a dashboard
        if('.json' in file):
            dash_path = './dashboards/' + file

            DASHBOARD_POSTER(lm_id, lm_key, lm_company, dash_group_id, dash_path)
elif(args_dict['dash'] != None):
    dash_id = args_dict['dash']
    DASH_OBTAIN(lm_id, lm_key, lm_company, dash_id)

print('########')
print('########')
print('')
print('Success!')
print('')
print('########')
print('########')
