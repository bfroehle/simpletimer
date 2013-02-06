A Simple Python Timer
=====================

Class based interface
---------------------

Procedural usage.

    >>> from simpletimer import TicToc
    >>> timer = TicToc()
    >>> timer.tic()
    >>> for i in range(10000):
    ...     pass
    >>> timer.toc()
    Elapsed time is 4.619975 seconds.
    >>> t.elapsed
    4.6199750900268555


Automatic starting and stopping using a with statement.

    >>> with TicToc():
    ...     time.sleep(2)
    ...
    Elapsed time is 2.002168 seconds.

Custom format strings.

    >>> with TicToc("{elapsed:7.3f}\n"):
    ...     time.sleep(2)
    ...
      2.002

Pass a barrier function as the keyword argument `barrier` to synchronize
processes before the timer starts and stops. For example, you could use
the `Barrier` method of an MPI communicator:

    >>> from mpi4py import MPI
    >>> with TicToc(barrier=MPI.COMM_WORLD.Barrier):
    ...    pass
    Elapsed time is 0.000027 seconds.

MATLAB-like interface
---------------------

A simple MATLAB-like interface is also available. Advanced features
like multiple timers are not implemented.

    >>> from simpletimer import tic, toc
    >>> tic(); time.sleep(4); toc()
    Elapsed time is 4.003983 seconds.
