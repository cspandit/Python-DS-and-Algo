import functools
import logging
import time


def decorated_by(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        inp = [i for i in kwargs.values()]
        for x in list(args) + inp:
            if not isinstance(x, int):
                raise TypeError('%s function only except integers' % decorated.__name__)

        start = time.time()
        x = decorated(*args, **kwargs)
        end = time.time()
        delt = end - start


        logging.basicConfig(level=logging.DEBUG, filename='test.log', filemode='w',
                            format='%(asctime)s :  %(process)d - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger("decorator logging")
        logger.info("%s took %.02f" % (decorated.__name__, delt))
        return x
    return inner

@decorated_by
def add(x, y):
    time.sleep(2)
    return x+y

print(add('',3))
