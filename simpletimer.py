"""Measure execution time.

This module provides a class based interface (`TicToc`) and function
based interface (`tic` and `toc`).  The `TicToc` class may be used as
a context manager.
"""

#-----------------------------------------------------------------------------
#  Copyright (C) 2013 Bradley Froehle
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from __future__ import print_function
import time

__all__ = ['TicToc', 'tic', 'toc']

class TicToc():
    """A simple timing class.

    Examples
    --------

    Procedural usage.

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

    Barriers
    --------

    Pass a barrier function as the keyword argument `barrier` to synchronize
    processes before the timer starts and stops. For example, you could use
    the `Barrier` method of an MPI communicator::

    >>> from mpi4py import MPI
    >>> with TicToc(barrier=MPI.COMM_WORLD.Barrier):
    ...    pass
    Elapsed time is 0.000027 seconds.
    """

    default_msg='Elapsed time is {elapsed:f} seconds.\n'

    def __init__(self, msg=default_msg, barrier=None):
        self._msg = msg
        self._barrier = barrier

    def reset(self):
        if hasattr(self, 'start_time'):
            del self.start_time
        if hasattr(self, 'end_time'):
            del self.end_time

    def tic(self):
        """Start (or restart) the timer."""
        self.reset()
        if self._barrier is not None:
            self._barrier()
        self.start_time = time.time()

    def toc(self):
        """Stop the timer and print the message.

        The elapsed time is available in the 'elapsed' attribute.
        """
        if not self.is_started:
            raise RuntimeError("Timer not yet started.")
        if self._barrier is not None:
            self._barrier()
        self.end_time = time.time()
        if self._msg:
            print(self._msg.format(elapsed=self.elapsed), end='')

    @property
    def is_started(self):
        return hasattr(self, 'start_time')
    @property
    def is_ended(self):
        return hasattr(self, 'end_time')

    @property
    def elapsed(self):
        if not self.is_started:
            raise RuntimeError("Timer not yet started.")
        elif self.is_ended:
            return self.end_time - self.start_time
        else:
            return time.time() - self.start_time

    def __float__(self):
        return self.elapsed

    def __str__(self):
        if self.is_started:
            return self.default_msg.format(elapsed=self.elapsed).rstrip('\n')
        else:
            return "Timer not yet started."

    def __enter__(self):
        self.tic()
        return self
    def __exit__(self, type, value, traceback):
        self.toc()

_tictoc = TicToc()
tic = _tictoc.tic
toc = _tictoc.toc
