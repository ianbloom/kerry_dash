# kerry_dash

## Introduction
This project was inspired by [Kerry's LogicMonitor Dashboards](https://github.com/kdevilbiss/Dashboards).  Many of Kerry's Dashboards rely on built in 'Devices by Type' groups to properly apply.  These device groups are traditionally applied account wide, which offers a challenge to LogicMonitor's MSP customers.  These MSPs would like access to many of the automated features available to LogicMonitor Internal IT customers, but on a customer by customer basis.

## Installation

To install this package, run the following at your command line:

```
git clone https://github.com/ianbloom/kerry_dash.git
```

Then, run the following:

```
sudo python setup.py install
```

Included in this repo is an example key file (key_file.txt).  Feel free to replace the dummy values in this file with values corresponding to your LogicMonitor API credentials.  This file does not need to be in the same directory as the script.

## Setup

This repository comes out of the box with a few recommended dashboards, but it is possible to extract your favorite tokenized dashboards for use as well.  

__Note: The format of these dashboard templates is different from those extracted via UI, because dashboards extracted via UI cannot be manipulated using LM API v2 endpoints.__

There are two 'modes' in which subgroup_creater can run.  If the -dash argument is used, then the script will attempt to extract the dashboard of the specified ID.

## Usage

For information about the required variables, run the following:

```
python subgroup_creator.py -h
```

This script takes a -file argument and either a -group or -dash argument:
* _-file_ : Path to file containing API credentials
* _-group_ : The ID of a LogicMonitor device group to create dynamic subgroups and dashboards for
* _-dash_ : The ID of a LogicMonitor dashboard to extract

## Example

For my LogicMonitor account, I run the following to create dynamic subgroups for the device group with ID 42 and an associated dashboard group filled with the dashboards found in the ./dashboards directory:

```
python subgroup_creator.py -file keyfile.txt -group 42
```

To download a templatized version of the dashboard with ID 42 and place it in the ./dashboards directory:

```
python subgroup_creator.py -file keyfile.txt -dash 42
```

## Result

The creation of the following subgroups:
* Linux Servers
* Windows Servers
* Collectors
* Network

The creation of a dashboard group with the name of the selected device group and the ##defaultDeviceGroup## token set to the device group's full path.

The import of all dashboards in the ./dashboards folder.