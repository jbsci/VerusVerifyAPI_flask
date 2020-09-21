# VerusVerifyAPI

Simple API to verify messages, files, or filehashes with Verus. WIP.

### Dependencies

0. Python 3
1. requests
2. Flask
3. Flask-API
4. flask_sslify
5. ast

### Setup

1. Edit ```rpc_api.conf``` to specify parameters for the rpc client and the API. For the RPC configuration, either include the path to VRSC.conf or include the information in a dictionary like so:
```
confdict = { "rpcuser" : "$rpcuser", "rpcpassword" : "$rpcpassword", "rpcport" : $port }
```
2. If you wish to enable native SSL to avoid using a proxy/server like nginx, set ```SSL = yes``` and specify the locations for the key and certificate in ```rpc_api.conf```
3. Set any other desired parameter changes like the hostname or port. 
4. run ```./verusverifyapi.py.```

### Basic Usage

```
http://localhost:5000/verifymessage/?message=This%20is%20a%20test%20message&signer=jbsci@&signature=Af+4EQABQSA1qs5h3yc553W8ulMVU+cVhJgXnkXHeZyEvP7oX9Iiizq3LIY1kWCyrWromhRv7CO1mdViKffFd6jGku0SiCSM
```

### Input/Output

```
In: /verifymessage/?message=<message>&signer=<signer>&signature=<signature>
out: { valid : true|false }

In: /verifyhash/?hash=<filehash>&signer=<signer>&signature=<signature>
out: { valid : true|false }

In: /getid/?id=<identity>
out: Identity information
```

### Notes:

1. Messsages need to be properly URL encoded before being passed to API.
