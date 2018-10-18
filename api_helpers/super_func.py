from api_helpers.lm_api import *

# These functions occur a logical level higher than those in lm_api

def SUBGROUP_POSTER(_lm_id, _lm_key, _lm_account, _group_id):
    # First GET the name and properties of device group _group_id
    # Build HTTP query
    resource_path = f'/device/groups/{_group_id}'
    query_params  = ''
    data          = ''

    # Obtain response
    return_dict = LM_GET(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    body = json.loads(return_dict['body'])

    # Full path will be used in the definition of subsequent dynamic groups
    group_full_path = body['fullPath']

    # Now POST a dynamic device subgroup for network devices
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
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{group_full_path}" && isLinux()'
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
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{group_full_path}" && isWindows()'
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
    data_dict['appliesTo']   = f'join(system.staticgroups,",") =~ "{group_full_path}" && isNetwork()'
    data_dict['parentId']    = f'{_group_id}'
    data_dict['name']        = 'Network'

    # Convert data_dict to JSON string
    data = json.dumps(data_dict)
    return_dict = LM_POST(_lm_id, _lm_key, _lm_account, resource_path, query_params, data)
    print(return_dict['code'])
    print(return_dict['body'])

    return 0

def DASH_GROUP_POSTER(_lm_id, _lm_key, _lm_account):
    return 0

def GET_DEVICE_GROUP(_lm_id, _lm_key, _lm_account, _group_id):
    return 0