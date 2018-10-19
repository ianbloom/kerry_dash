from api_helpers.lm_api import *

# These functions occur a logical level higher than those in lm_api

def SUBGROUP_GETTER(_lm_id, _lm_key, _lm_account, _group_id):
    # GETS subgroup and returns full path
    # Build HTTP query
    resource_path = f'/device/groups/{_group_id}'
    query_params  = ''
    data          = ''

    # Obtain response
    return_dict = LM_GET(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    body = json.loads(return_dict['body'])

    # Full path will be used in the definition of subsequent dynamic groups
    group_full_path = body['fullPath']
    name            = body['name']

    return_dict['name'] = name
    return_dict['path'] = group_full_path

    return return_dict

def SUBGROUP_POSTER(_lm_id, _lm_key, _lm_account, _group_id, _group_full_path):
    # Build HTTP query
    resource_path = '/device/groups'
    query_params  = ''

    #################
    # Linux Servers #
    #################

    # Build data dictionary to be converted to JSON string
    data_dict                = {}
    data_dict['groupType']   = 'Normal'
    data_dict['description'] = 'Linux Servers'
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{_group_full_path}" && isLinux()'
    data_dict['parentId']    = f'{_group_id}'
    data_dict['name']        = 'Linux Servers'

    # Convert data_dict to JSON string
    data = json.dumps(data_dict)
    return_dict = LM_POST(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    print(return_dict['code'])
    print(return_dict['body'])

    ###################
    # Windows Servers #
    ###################

    # Build data dictionary to be converted to JSON string
    data_dict                = {}
    data_dict['groupType']   = 'Normal'
    data_dict['description'] = 'Windows Servers'
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{_group_full_path}" && isWindows()'
    data_dict['parentId']    = f'{_group_id}'
    data_dict['name']        = 'Windows Servers'

    # Convert data_dict to JSON string
    data = json.dumps(data_dict)
    return_dict = LM_POST(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    print(return_dict['code'])
    print(return_dict['body'])

    ###########
    # Network #
    ###########

    # Build data dictionary to be converted to JSON string
    data_dict                = {}
    data_dict['groupType']   = 'Normal'
    data_dict['description'] = 'Network Devices'
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{_group_full_path}" && isNetwork()'
    data_dict['parentId']    = f'{_group_id}'
    data_dict['name']        = 'Network'

    # Convert data_dict to JSON string
    data = json.dumps(data_dict)
    return_dict = LM_POST(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    print(return_dict['code'])
    print(return_dict['body'])

    return 0

def DASH_GROUP_POSTER(_lm_id, _lm_key, _lm_account, _name, _full_path):
    resource_path = '/dashboard/groups'
    query_params  = ''

    # Build data_dict
    data_dict = {}
    data_dict['name'] = _name
    data_dict['parentId'] = 1

    data_dict['widgetTokens']                   = []
    data_dict['widgetTokens'].append({})

    data_dict['widgetTokens'][0]['inheritList'] = []
    data_dict['widgetTokens'][0]['type']        = 'owned'
    data_dict['widgetTokens'][0]['name']        = 'defaultDeviceGroup'
    data_dict['widgetTokens'][0]['value']       = _full_path

    # Turn data dictionary into json string
    data = json.dumps(data_dict)

    return_dict = LM_POST(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    return return_dict

def DASHBOARD_POSTER(_lm_id, _lm_key, _lm_account, _dash_group_id, _exported_json):
    # Example of widgets config
#     "widgetsConfig" : {\n'
#  '    "33" : {\n'
#  '      "col" : 9,\n'
#  '      "sizex" : 4,\n'
#  '      "row" : 5,\n'
#  '      "sizey" : 4\n'
#  '    },\n'
    return 0