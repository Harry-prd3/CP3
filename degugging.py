import logging

logging.basicConfig(level=logging.DEBUG)

def buggy_function(a,b):
    result = a * b
    logging.debug(f"a: {a} b {b} reslut: {result}")
    return result

print(buggy_function("3",2))