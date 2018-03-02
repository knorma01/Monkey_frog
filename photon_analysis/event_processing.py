#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
event_processing.py: Python script that contains functions for event and epoch
processing.
"""


__author__ = "DM Brady"
__datewritten__ = "01 Mar 2018"
__lastmodified__ = "01 Mar 2018"


def EvtDict(evtlist=['correct', 'incorrect', 'iti_start', 'omission', 'premature', 'stimulus', 'tray']):
    """Takes in an ordered list of events and maps it to a dictionary. Keys are numbers starting at 1.
    >>> EvtDict(evtlist=['event1', 'event2']) == {'1': 'event1', '2': 'event2'}
    True
    """
    # Calculates how many keys we need for our dictionary
    dict_len = len(evtlist)
    # Makes a list of numerals (but they are strings) as our key values
    keys = [str(ind + 1) for ind in range(dict_len)]
    # zips keys with our evtlist and makes it a dictionary
    return dict(zip(keys, evtlist))