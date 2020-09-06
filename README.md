# VerusVerifyAPI

Simple API to verify messages, files, or filehashes with Verus. WIP.

### Dependencies

0. Python 3
1. requests
2. Flask
3. Flask-API

### Setup

1. Edit ```verusrpc.py``` to specify host information and either include the path to your VRSC.conf file or add RPC information via a dictionary:
```
confdict = { "rpcuser" : "$rpcuser", "rpcpassword" : "$rpcpassword", "rpcport" : $port }
```
2. run ```./verusverifyapi.py.```

### Basic Usage

```
http://localhost:5000/verifymessage/?message=This is a test message&signer=jbsci@&signature=Af+4EQABQSA1qs5h3yc553W8ulMVU+cVhJgXnkXHeZyEvP7oX9Iiizq3LIY1kWCyrWromhRv7CO1mdViKffFd6jGku0SiCSM
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
