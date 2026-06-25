# -*- coding: utf-8 -*-
"""A Turing machine simulator skeleton.

    Accepting '#'
    =============

    >>> from turing_machine import TuringMachine

    Instantiate the machine with particular transitions.

    >>> one_hash = TuringMachine(
    ...     {
    ...         ('q0', '#'): ('saw_#', '#', 'R'),
    ...         ('saw_#', ''): ('qa', '', 'R'),
    ...     }
    ... )

    Check whether it accepts a string:

    >>> one_hash.accepts('#')
    True

    >>> one_hash.accepts('##')
    False

    Check whether it rejects a string:

    >>> one_hash.rejects('#')
    False

    >>> one_hash.rejects('##')
    True

"""

import logging
from itertools import islice


class TuringMachine:

    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def run(self, input_):
        if isinstance(input_, str):
            input_ = list(input_)
    
        left_hand_side = []
        state = self.start_state

        if (input_):
            symbol = input_[0]
            right_hand_side = input_[1:]
        else:
            symbol = self.blank_symbol
            right_hand_side = []

        while True:
            config = {"state": state, 
                  "left_hand_side": left_hand_side,
                  "symbol": symbol,
                  "right_hand_side": right_hand_side}
            
            if state == self.accept_state:
                yield "Accept", config
                break

            if state == self.reject_state or (state,symbol) not in self.transitions:
                yield "Reject", config
                break

            yield None , config

            if (state,symbol) in self.transitions:
                next_state, new_symbol, movement = self.transitions[(state,symbol)]
                symbol = new_symbol
                state = next_state
                if movement == 'L':
                    right_hand_side.insert(0,symbol)
                    if left_hand_side:
                        symbol = left_hand_side.pop(0)
                    else:
                        symbol = self.blank_symbol
                else:
                    left_hand_side.insert(0,symbol)
                    if right_hand_side:
                        symbol = right_hand_side.pop(0)
                    else:
                        symbol = self.blank_symbol


    def accepts(self, input_, step_limit=100):
        for (action, config) in islice(self.run(input_) , step_limit):
            if (action == "Accept"):
                return True
            elif (action == "Reject"):
                return False
        logging.warning("reached step limit without halting. please increase it")
        return None

    def rejects(self, input_, **kwargs):
        result = self.accepts(input_, **kwargs)
        if result: return False
        elif (result == False): return True
        else: return None

    def debug(self, input_, step_limit=100, colored=False):
        """Print the execution configuration of the machine per transition for debugging.

        :param input_: the input string or list.
        :param step_limit: the maximum number of steps to output.
        :param colored: True to output colored boundaries in terminal.
        """
        # TODO: Loop over the steps yielded by run() up to step_limit and print the tape configuration.
        # E.g., print the state and the tape with the head highlighted in brackets like: left[symbol]right
        for (action, config) in islice(self.run(input_) , step_limit):
            print(f'{config["state"]}: {''.join(reversed(config["left_hand_side"]))}[{str(config["symbol"])}]{''.join(config["right_hand_side"])}')
            