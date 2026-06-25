# -*- coding: utf-8 -*-
from turing_machine import TuringMachine
from test_turing_machine_example1 import print_states

#create the Turing machine
transitions = {

    ('q0','0'): ('q0','0','R'),
    ('q0','1'): ('q0','1','R'),
    ('q0',''): ('q1','','L'),

    ('q1','1'): ('q2','','L'),
    ('q1','0'): ('qr','0','R'),
    ('q1',''): ('qr','','R'),

    ('q2','1'): ('q2','1','L'),
    ('q2','0'): ('q3','1','L'),

    ('q3','1'): ('q3','1','L'),
    ('q3','0'): ('qr','0','R'),
    ('q3',''): ('qa','','R'),
}

if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w)
        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 11111

    # SHOULD ACCEPT
    run("11101111")
    #     # outputs 1111111
    run("0111")
    # outputs 111
    run('1001')
    # reject
