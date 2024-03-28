# That library use secure connecting for MQTT IoT devices

> NOTE:
> MQTT is a default IoT protocol and he hasn't secure.
> It lib can be used for unstable connection.

## Default tests:

### Firstly, setup server:

`python server/server.py`
u can get green output, it signal about success config
### Runing tests:

`python test/test_connection.py`
for get data to connection(port, ip, topic, broker)

`python test/test_msg.py`
for example testing message sender 

### Using in user's projects:

```python
from server.server import Setup

if __name__ == main:
    server = Setup()
    server.run()
```