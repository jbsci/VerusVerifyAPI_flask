# VerusVerifyAPI

Simple API to verify messages, files, or filehashes with Verus. WIP.

### Setup

1. Edit ```verusrpc.py``` to either include the path to your config file with RPC auth info or add custom auth info via a dictionary
2. run ```./verusverifyapi.py.``` Defaults to localhost:5000

### Basic Usage

```
http://localhost:5000/message=This is a test message?Signer=jbsci@&Signature=Af+4EQABQSA1qs5h3yc553W8ulMVU+cVhJgXnkXHeZyEvP7oX9Iiizq3LIY1kWCyrWromhRv7CO1mdViKffFd6jGku0SiCSM
```

### Inputs

```
In: /message=<message>?Signer=<Signer>&Signature=<Signature>
out: { valid : true|false }

In: /filehash=<filehash>?Signer=<Signer>&Signature=<Signature>
out: { valid : true|false }

In: /getid=<identity>
out: verbose identity information
```
