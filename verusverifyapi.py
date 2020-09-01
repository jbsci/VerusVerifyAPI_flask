#!/usr/bin/env python

'''
Written 2020 by Jonathan Barnes <jonathan@jbsci.org>

Basic Functionality:

    localhost:5000/$query=$queryinfo?Signer=$signer&Signature=$signature

    example:

    localhost:5000/message=This is a test message?Signer=jbsci@&Signature=Af+4EQABQSA1qs5h3yc553W8ulMVU+cVhJgXnkXHeZyEvP7oX9Iiizq3LIY1kWCyrWromhRv7CO1mdViKffFd6jGku0SiCSM
    

Requires verusrpc.py, needs some setup for where to locate the rpc information before running
'''

#-# Imports #-#

import os,sys
import socket
import json
import verusrpc as vrpc
from flask import Flask, request, url_for
from urllib.parse import unquote
from flask_api import FlaskAPI, status, exceptions 

#--# Definitions #--#

app = FlaskAPI(__name__)

#---# Functions #---#

def verusverify(thing_to_verify, signer, signature, method, rpcid):
    '''
    Uses given rpc method to perform verification of a File (verifyfile), Filehash (verifyhash), 
    or message (verifymessage)
    '''
    result = vrpc.verusquery(method, [signer, signature, thing_to_verify], rpcid=rpcid)
    return result

def verusidentity(identity):
    '''
    Queries RPC to check if identity exists and returns information
    '''
    result = vrpc.verusquery("getidentity", [identity], rpcid="getidentity")
    return result


#----# API #----#

@app.route("/filehash=<FileHash>", methods=["GET", "POST"]) 
def filehash(FileHash):
    keys = list(request.args.keys())
    if 'Signature' and 'Signer' not in keys:
        return '{"error" : 1, "error_text":"Missing Signature and/or Signer"}'
    signature   =   '+'.join(request.args['Signature'].split(' '))
    signer  =   request.args['Signer']
    if FileHash is not None:
        fh = FileHash
        result = verusverify(fh, signer, signature, 'verifyhash', rpcid='verifyhash')['result']
        if result:
            return '{"valid" : true}'
        else:
            return '{"valid" : false}'
    else:
        return '{"error" : 2, error_text : "Missing Filehash"}'

@app.route("/message=<Message>", methods=["GET", "POST"]) 
def message(Message):
    keys = list(request.args.keys())
    if 'Signature' and 'Signer' not in keys:
        return '{"error" : 1, "error_text":"Missing Signature and/or Signer"}'
    signature   =   '+'.join(request.args['Signature'].split(' '))
    signer  =   request.args['Signer']
    if Message is not None:
        message = Message
        result =  verusverify(message, signer, signature, 'verifymessage', rpcid='verifymessage')['result']
        if result:
            return '{"valid" : true}'
        else:
            return '{"valid" : false}'
    else:
        return '{"error" : 2, error_text : "Missing Message"}'

@app.route("/getid=<verusid>", methods=["GET", "POST"])
def getid(verusid):
    return str(verusidentity(verusid))
    



#-----# Run #-----#

if __name__ == '__main__':
    app.run()
