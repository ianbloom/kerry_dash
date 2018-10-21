from api_helpers.super_func import *
from api_helpers.lm_api import *
from pprint import pprint
import argparse
import os
import sys

def DASH_OBTAIN(lm_id, lm_key, lm_company, dash_id):
	resource_path = f'/dashboard/dashboards/{dash_id}'
	query_params  = ''
	data          = ''

	# Obtain response
	return_dict = LM_GET(lm_id, lm_key, lm_company, resource_path, query_params, data)
	dash_body = json.loads(return_dict['body'].decode())

	# Remove identifying information
	dash_body.pop('id')
	dash_body.pop('groupId')
	dash_body.pop('groupName')
	dash_body.pop('fullName')
	dash_body.pop('widgetTokens')

	# Obtain widgetsConfig which will help us build a widgets array
	widgets_config = dash_body['widgetsConfig']

	resource_path = f'/dashboard/dashboards/{dash_id}/widgets'
	query_params  = ''
	data          = ''

	# Obtain response
	return_dict = LM_GET(lm_id, lm_key, lm_company, resource_path, query_params, data)
	widget_list = json.loads(return_dict['body'].decode())
	# widget_items will be iterated through and searched for id
	widget_items = widget_list['items']

	# Iterate through widgets_config and initialize widgets_array
	widgets_array = []
	for widget_id, position in widgets_config.items():
		# iterate through widget_items and match on id
		for item in widget_items:
			# One is a string and one is an int, normalize
			if(int(widget_id) == int(item['id'])):
				# Remove identifying information
				item.pop('dashboardId')

				# Initialize dictionary to place in widgets array
				widget_array_dict = {}
				widget_array_dict['config'] = item
				widget_array_dict['position'] = position
				widgets_array.append(widget_array_dict)
	dash_body['widgets'] = widgets_array

	# Replaced with widget property
	dash_body.pop('widgetsConfig')
	dash_body.pop('groupFullPath')

	# Iterate through widgets, pop id from each config object post build
	for widget in dash_body['widgets']:
		# It's been done already?
		widget['config'].pop('id', None)
		widget['config'].pop('dataSourceId', None)

		# Remove ids from datapoint objects
		if('dataPoint' in widget['config'].keys()):
			widget['config']['dataPoint'].pop('dataPointId', None)
			widget['config']['dataPoint'].pop('dataSourceId', None)

		# Remove ids from graphInfo -> dataPoints
		if('graphInfo' in widget['config'].keys()):
			widget['config']['graphInfo'].pop('id', None)
			for dp in widget['config']['graphInfo']['dataPoints']:
				dp.pop('id', None)
				dp.pop('customGraphId', None)
				dp.pop('dataPointId', None)
				dp.pop('dataSourceId', None)

		# Remove ids from bigNumberInfo
		if('bigNumberInfo' in widget['config'].keys()):
			for dp in widget['config']['bigNumberInfo']['dataPoints']:
				dp.pop('id', None)
				dp.pop('customGraphId', None)
				dp.pop('dataPointId', None)
				dp.pop('dataSourceId', None)

		if('columns' in widget['config'].keys()):
			for cl in widget['config']['columns']:
				cl.pop('dataPointId', None)

	print('++++++++')
	print('++++++++')
	pprint(dash_body)

	# Collect name for use as filename 
	dash_name = dash_body['name']
	dash_name = dash_name.replace(':', '_')

	# Convert the dash_body dictionary back into a string
	dash_body_string = json.dumps(dash_body)

	file = open(f'./kerry_dash/kerry_dash/dashboards/{dash_name}.json', 'w')
	file.write(dash_body_string)
	file.close()