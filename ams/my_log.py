import logging

log = logging.getLogger(__name__)  
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
log.addHandler(stream_handler)

#formatter - logging.Formatter('%(asctime)s-%(levelname)s : %(message)s')

log.debug('Hi Erik')