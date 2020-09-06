'''
Simple wrapper to query the verus RPC client and perform various operations. 

Needs configuration specified for RPC authentication, either with the verus 
RPC configuration file path or user input dictionary formatted as follows:
    
    { "rpcuser" : "$username", "rpcpassword" : "$rpcpassword", "rpcport" : $port } 

Written 2020 by Jonathan Barnes <j@jbsci.dev>
'''

#-# imports #-#

import requests
from requests.auth import HTTPBasicAuth

#--# Definitions #--#

rpchost = 'http://localhost'

#Specifies either path to configuration file or dictionary with configuration information.
#Default for the verusquery function is use the confpath

confdict = {}
confpath = ''

#---# Functions #---#

def rpcdetails(conffile):
    '''
    Reads in config file and stores in dictionary for use
    '''
    if len(conffile) == 0:
        print("ERROR: Specify a configuration file with RPC login information")
    return { line.split('=')[0] : line.split('=')[1].strip('\n') for line in open(conffile, 'r')}

def verusquery(method, params, rpcid= " ", rpcinfo=rpcdetails(confpath), host=rpchost):
    '''
    Function to query the Verus RPC client. Builds payload based on method and parameters.
    
    Default configuration is from the confpath specified above.
    '''
    if type(params) != list:
        print("ERROR: Params must be given as a list")
    payload = {"jsonrpc" : "1.0", "id": rpcid , "method" : method, "params": params}
    response = requests.post(host+':'+rpcinfo['rpcport'], json=payload, headers={'content-type': 'text/plain;'}, auth=HTTPBasicAuth(rpcinfo['rpcuser'], rpcinfo['rpcpassword'])).json()
    return response
