import logging

# logging setting 

logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%(asctime)s-%(name)s-%(message)s %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)
# crate logger for ArthrmaticApp
logger=logging.getLogger("ArthemathicApp")

# here create function add,sub,mut,div

def add(a,b):
    result=a+b
    logger.debug(f"Addition {a}+{b} = {result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtraction {a}-{b} = {result}")
    return result

def Multi(a,b):
    result=a*b
    logger.debug(f"multiplication {a}*{b} = {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Division {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero not allowed")
        return None

add(4,6)
subtract(10,5)
Multi(12,6)
divide(20,0)




