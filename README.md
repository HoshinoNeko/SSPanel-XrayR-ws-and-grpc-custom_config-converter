# SSPanel-XrayR-ws-and-grpc-custom_config-converter
Convert XrayR recommend custom_config for sspanel to current clash compatible custom_config

# Usage
Convert custom_config from
```
{
    "offset_port_node":"10000",
    "offset_port_user":"443",
    "server_sub":"",
    "host":"",
    "alter_id":"0",
    "network":"ws",
    "security":"tls",
    "path":"\/videopreview",
    "enable_vless":"1"
}
```
to
```
{
    "offset_port_node":"10000",
    "offset_port_user":"443",
    "server_sub":"",
    "host":"",
    "alter_id":"0",
    "network":"ws",
    "security":"tls",
    "ws-opts": {
      "path": "\/videopreview",
      "headers": {
        "Host": ""
      }
    },
    "path":"\/videopreview",
    "enable_vless":"1"
}
```
And the same to grpc
```
{
    "offset_port_node": "10000",
    "offset_port_user": "443",
    "server_sub": "",
    "host": "",
    "alter_id": "0",
    "network": "grpc",
    "security": "tls",
    "servicename": "",
    "enable_vless": "1"
}
```
```
{
    "offset_port_node": "10000",
    "offset_port_user": "443",
    "server_sub": "",
    "host": "",
    "alter_id": "0",
    "network": "grpc",
    "security": "tls",
    "servicename": "",
    "enable_vless": "1",
    "grpc-opts": {
        "grpc-service-name": ""
    }
}
```
This change will give clash the correct configuration
# Instrucation
Before doing anything you should check if the match condition works for your node.
```
# Make sure you have python and python-pip installed before
# Install requirements
pip3 install mysql.connector
# For websocket node
python3 ws-opts.py
# For grpc node
python3 grpc-opts.py
```