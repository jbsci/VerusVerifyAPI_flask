#!/usr/bin/env python

'''
Basic Functionality:

    $host/$querytype/?$query=$queryinput&signer=$signer&signature=$signature

    example:

    $host/verifymessage/?message=This is a test message&signer=jbsci@&signature=Af+4EQABQSA1qs5h3yc553W8ulMVU+cVhJgXnkXHeZyEvP7oX9Iiizq3LIY1kWCyrWromhRv7CO1mdViKffFd6jGku0SiCSM
    

Requires verusrpc.py (included in this repo) and configuration via rpc_api.conf

Written 2020 by Jonathan Barnes <j@jbsci.dev>
'''

#-# Imports #-#

import verusrpc as vrpc
from flask import Flask, request
from flask_api import FlaskAPI, status, exceptions 
from flask_sslify import SSLify


#--# Definitions #--#

app = FlaskAPI(__name__)

#---# Configuration #---#

class readconfig:
    def __init__(self):
        for line in open('rpc_api.conf', 'r'):
            if line.find('#') >= 0:
                line = line.split('#')[0]
            line = line.strip()
            if len(line) > 0:
                segments = line.split('=')
                inparam = segments[0].strip()
                inval = segments[1].strip()
                if inparam == 'apiport':
                    self.port = int(inval)
                elif inparam == 'apihost':
                    self.host = inval
                elif inparam == 'SSL':
                    if inval.upper() == 'YES':
                        self.ssl = True
                    else:
                        self.ssl = False
                elif inparam == 'SSL_KEY':
                    self.sslkey = inval
                elif inparam == 'SSL_CRT':
                    self.sslcrt = inval

apiconf = readconfig()
if apiconf.ssl:
    context = (apiconf.sslcrt, apiconf.sslkey)
    sslify = SSLify(app)

#----# Functions #----#

def verusverify(thing_to_verify, signer, signature, method, rpcid):
    '''
    Uses given rpc method to perform verification of a File (verifyfile), Filehash (verifyhash), 
    or message (verifymessage)
    '''
    result = vrpc.verusquery(method, [signer, signature, thing_to_verify], rpcid=rpcid)
    return result

def verusidentity(identity):
    '''
    Queries RPC to check if identity exists and returns information. 

    Can use identity or identity address.
    '''
    result = vrpc.verusquery("getidentity", [identity], rpcid="getidentity")
    if result["result"]:
        del result['result']['cansignfor']
        del result['result']['canspendfor']
        return result
    else:
        return result


#-----# API #-----#

@app.route("/verifyhash/", methods=["GET"]) 
def filehash():
    keys = list(request.args.keys())
    if 'hash' not in keys:
        return {"error" : 2, "error_detail" : "No filehash specified"},400
    elif 'signature' and 'signer' not in keys:
        return {"error" : 1, "error_text":"Missing signature and/or signer"},400
    signature   =   '+'.join(request.args['signature'].split(' '))
    signer  =   request.args['signer']
    fh = request.args['hash']
    if fh is not None:
        result = verusverify(fh, signer, signature, 'verifyhash', rpcid='verifyhash')['result']
        if result:
            return {"valid" : "true"}
        else:
            return {"valid" : "false"}
    else:
        return {"error" : 2, "error_detail" : "No filehash specified"}

@app.route("/verifymessage/", methods=["GET"]) 
def message():
    keys = list(request.args.keys())
    if 'message' not in keys:
        return {"error" : 2, "error_detail" : "No message specified"},400
    elif 'signature' and 'signer' not in keys:
        return {"error" : 1, "error_text":"Missing signature and/or signer"},400
    signature   =   '+'.join(request.args['signature'].split(' '))
    signer  =   request.args['signer']
    message = request.args['message']
    if message is not None:
        result =  verusverify(message, signer, signature, 'verifymessage', rpcid='verifymessage')['result']
        if result:
            return {"valid" : "true"}
        else:
            return {"valid" : "false"}
    else:
        return {"error" : 2, "error_detail" : "No message specified"}

@app.route("/getid/", methods=["GET"]) 
def getid():
    if request.args['id'] is None:
        return {"error" : 2, "error_detail" : "No identity specified"},400
    else:
        return verusidentity(request.args['id'])
    



#------# Run #------#

if __name__ == '__main__':
    if apiconf.ssl:
        context = (apiconf.sslcrt, apiconf.sslkey)
        app.run(host=apiconf.host, port=apiconf.port, ssl_context = context)
    else:
        app.run(host=apiconf.host, port=apiconf.port)
