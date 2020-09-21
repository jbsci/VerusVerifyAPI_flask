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
All configuration is handled in the ```rpc_api.conf``` file. There are two sections for configuring both the RPC information and the specifications for the API. The configuration options are as follows:

#### RPC Configuration

1. ```rpchost``` Specifies the hostname for the RPC server
2. ```rpcconf``` Specifies the configuration information for the RPC server, namely the port, username and password. This can either be given as the path to a configuration file, like VRSC.conf, or as a dictionary formatted like so:
```
confdict = { "rpcuser" : "$rpcuser", "rpcpassword" : "$rpcpassword", "rpcport" : $port }
```

#### API Configuration
1. ```apiport``` specifies the port you want the API to run on, defaults to 5000. 
2. ```apihost``` Specifies the host for the API, defaults to localhost. Set to 0.0.0.0 to be accessible from a network without a proxy/server. 
3. ```SSL``` Toggles native ssl via yes|no, if yes, then you need to also specify the key and sertificates
4. ```SSL_KEY``` and ```SSL_CRT``` specify the path/name for the SSL key and certificate respectively. 

#### Running the API
After setup, just run ```./verusverifyapi.py```

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
