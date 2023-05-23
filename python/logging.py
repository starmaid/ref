import logging

logging.basicConfig(filename=app_log_path, level=logging.ERROR,
                    format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')


logging.error('whatever')