# VerusVerifyAPI

Simple API to verify messages, files, or filehashes with Verus. WIP.

### Setup

1. Edit ```verusrpc.py``` to either include the path to your config file with RPC auth info or add custom auth info via a dictionary
2. run ```./verusverifyapi.py.``` Defaults to localhost:5000

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
out: verbose identity information
```

### Notes:

1. Messsages need to be properly URL encoded before being passed to API.
