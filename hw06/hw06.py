
passphrase = '*** PASSPHRASE HERE ***'


def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    'a874c00444b93ed81bc8dcde469ba5f4f3e7ddfcf994f7b8781821a1'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()