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

This repository comes out of the box with a few recommended dashboards, but it is possible to extract your favorite tokenized dashboards for use as well.  Note: The format of these dashboard templates is different from those extracted via UI, because dashboards extracted via UI cannot be manipulated using LM API v2 endpoints.

There are two 'modes' in which subgroup_creater can run.  If the -dash argument is used, then the script will attempt to extract the dashboard of the specified ID.