#!/usr/bin/env python

'''
Written 2020 by Jonathan Barnes <jonathan@jbarnes.dev>

Basic Functionality:
    
    */hash?FileHash=XXXX&Signature=YYYYYY&Signer=ZZZZZZ -> {valid:T|F}

Requires verusrpc.py, needs some setup for where to locate the rpc information before running
'''

#-# Imports #-#

import os,sys, argparse
import socket
import verusrpc as vrpc
from flask import Flask, request, url_for
from urllib.parse import unquote
from flask_api import FlaskAPI, status, exceptions 

#--# Definitions #--#

rpc_port = 27486
url = 'http://localhost:{:d}'.format(rpc_port)
app = FlaskAPI(__name__)

#---# Functions #---#

def verusverify(thing_to_verify, signer, signature, method, rpcid, url=url):
    '''
    Uses given rpc method to perform verification of a File (verifyfile), Filehash (verifyhash), 
    or message (verifymessage)
    '''
    result = vrpc.verusquery(method, [signer, signature, thing_to_verify], url, rpcid=rpcid)
    return result

@app.route("/hash", methods=["GET", "POST"]) 
def verifyapi():
    keys = list(request.args.keys())
    if 'Signature' and 'Signer' not in keys:
        return 'ERROR: Signature and Signer required'
    signature   =   '+'.join(request.args['Signature'].split(' '))
    signer  =   request.args['Signer']
    if 'Filehash' in keys:
        fh = request.args['Filehash']
        return str(verusverify(fh, signer, signature, 'verifyhash', rpcid='verifyhash'))
    elif 'Message' in keys:
        message = request.args['Message']
        return str(verusverify(message, signer, signature, 'verifymessage', rpcid='verifyfilehash'))
    elif 'File' in keys:
        Filebin = request.args['File']
        return str(verusverify(Filebin, signer, signature, 'verifyfile', rpcid='verifyfile'))
    else:
        return "ERROR: Please specify Filehash, Message, or File binary"

#----# Run #----#

if __name__ == '__main__':
    app.run(debug=False)
