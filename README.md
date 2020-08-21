# VerusVerifyAPI

Simple API to verify messages, files, or filehashes with Verus. WIP.

### Setup

1. Edit ```verusrpc.py``` to either include the path to your config file with RPC auth info or add custom auth info via a dictionary
2. run ```./verusverifyapi.py.``` Defaults to localhost:5000

### Usage

```
http://localhost:5000/hash?Message=$message&Signer=$signer&Signature=$signature
```
