def checklength(query:str,limit:int):
    if len(query) > limit:
        raise Exception( f'Words exceed {limit}')