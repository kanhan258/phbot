from phBot import *
import phBotChat

import re
import struct
from time import sleep

def handle_chat(data):
    if data[0] == 7:
        msg_len = struct.unpack_from('H', data, 1)[0]
        msg = struct.unpack_from(str(msg_len) + 's', data, 1 + 2)[0].decode('latin1')

        m = re.findall(r'(\d+)', msg)
        if m and len(m) >= 2:
            if msg.find('+') != -1:
                result = int(m[0]) + int(m[1])
            else:
                   result = int(m[0]) * int(m[1])

            sleep(1.0)

            log('Sending result %s' % str(result))
            if msg.find('.validate') != -1:
                phBotChat.All('.validate' + str(result))
            else:
                phBotChat.All(str(result))
    elif data[0] == 2:
        name_len = struct.unpack_from('H', data, 1)[0]
        name = struct.unpack_from(str(name_len) + 's', data, 1 + 2)[0].decode('latin1')

        if name == 'RemoLogger' or name == 'Bot':
            msg_len = struct.unpack_from('H', data, 1 + 2 + name_len)[0]
            msg = struct.unpack_from(str(msg_len) + 's', data, 1 + 2 + name_len + 2)[0].decode('latin1')

            m = re.findall(r'(\d+)', msg)
            if m and len(m) >= 2:

                if msg.find('+') != -1:
                    result = int(m[0]) + int(m[1])
                else:
                    result = int(m[0]) * int(m[1])

                sleep(1.0)

                log('Sending result %s' % str(result))
                phBotChat.Private(name, str(result))

def handle_joymax(opcode, data):
    if opcode == 0x3026 and get_locale() == 22:
        handle_chat(data)
    return True

log('[%s] Loaded' % __name__)
