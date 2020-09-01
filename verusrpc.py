'''
Helper module to query the verus RPC client and perform various operations

Needs configuration file specified for RPC authentication

Written 2020 by Jonathan Barnes <jonathan@jbarnes.dev>
'''

#-# imports #-#

import json
import requests
from requests.auth import HTTPBasicAuth

#--# Definitions #--#

#Specifies path to configuration file, wont work without it
confpath = ''

#---# Functions #---#

def rpcdetails(conffile = confpath):
    '''
    Reads in config file and stores in dictionary for use
    '''
    if len(conffile) == 0:
        print("ERROR: Specify a configuration file with RPC login information")
    return { line.split('=')[0] : line.split('=')[1].strip('\n') for line in open(conffile, 'r')}

def verusquery(method, params, rpcid= " ", rpcinfo=rpcdetails()):
    '''
    Function to query the Verus RPC client. Builds payload based on method and parameters

    If querying a remote system, specify the RPC login information with a dictionary like so: 
        { "rpcuser" : "$username", "rpcpassword" : "$rpcpassword" } 
    '''
    if type(params) != list:
        print("ERROR: Params must be given as a list")
    payload = {"jsonrpc" : "1.0", "id": rpcid , "method" : method, "params": params}
    response = requests.post('http://localhost:{}'.format(rpcinfo['rpcport']), json=payload, headers={'content-type': 'text/plain;'}, auth=HTTPBasicAuth(rpcinfo['rpcuser'], rpcinfo['rpcpassword'])).json()
    return response
