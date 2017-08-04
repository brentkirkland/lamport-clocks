# lamport-clocks

This repo is an implementation of lamport clocks for a distributed systems course.

Lamport logical clocks are used to order events capturing causality or happens before relationship
between events. An event e happens before another event f (denoted by e → f) iff:
* the same process executes e and f and e is executed before f,
* e is the send event of a message m (send(m)) and f is the corresponding receive of a message
m (receive(m)), or
* ∃h | e → h ∧ h → f

### To Run:

Open three local terminals and run

`./asg1 [testfile #]` or `python asg1.py [testfile #]`

Where testfile # is the testfile that is unique for each terminal. See the testcases for examples.
