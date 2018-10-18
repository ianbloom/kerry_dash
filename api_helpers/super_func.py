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
    print(group_full_path)


    return 0