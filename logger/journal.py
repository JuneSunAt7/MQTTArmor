
def write_log(info):
    with open('mqtt.log', 'a') as log:
        log.write(str(info) + "\n")
