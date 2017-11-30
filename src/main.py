"""
Module to train autogenerating docs
"""
def inc(arg):
    """
    Function increment given argument

    >>> inc(1)
    2

    :param arg: Argument to increment
    :return: arg + 1
    :rtype: integer
    """
    return arg1 + 1, arg2


def iDontCare(nick, *, x=1):
    """
    Function greet given person
    
    >>> iDontCare('Cukierku')
    'Hej Cukierku:*'
    
    :param nick: Nickname to greet
    :param x: Number of greetings (default=1)
    :return: Greeting text
    :type: string
    """
    return f"Hej {nick}:* "*x
