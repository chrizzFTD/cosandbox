import logging
import os, fnmatch
import sys

logging.basicConfig(level=logging.INFO) #El tipo de mensaje que quiero ver, y existen warning, critical, debugging and info
logger = logging.getLogger(__name__)

def parse_args():

    module_path = os.path.dirname(os.path.abspath(__file__))

    config = {}
    config['api-endpoint'] = 'http://dpydalmvpd301.sl.bluecloud.ibm.com:8081'

    for iarg in range(1, len(sys.argv)):
        arg = sys.argv[iarg]
        if arg.startswith("--api-endpoint="):
            config['api-endpoint'] = arg.split("=", 1)[1]

        else:
            logger.warning("Unexpected argument: %s" % (arg))
            return None

    return config
    # return module_path

if __name__ == '__main__':
    resultado = parse_args()
    print(resultado)