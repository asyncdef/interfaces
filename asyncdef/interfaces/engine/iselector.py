"""IProcessor extension that manages IO events use a Select implementation."""

import typing

import iface

from . import iprocessor


class IFileLike(iface.Iface):

    """A file-like object that exposes a file descriptor integer."""

    @iface.method
    def fileno(self) -> int:
        """Return an integer file descripter for the object."""
        raise NotImplementedError()


class ISelector(iprocessor.IProcessor):

    """A processor that handles IO events using a selector."""

    @iface.method
    def add_reader(
            self,
            fd: IFileLike,
            callback: typing.Callable[[IFileLike], typing.Any],
    ) -> None:
        """Add a file descriptor to the processor and wait for READ.

        Args:
            fd (IFileLike): Any obect that exposes a 'fileno' method that
                returns a valid file descriptor integer.
            callback (typing.Callable[[IFileLike], typing.Any]): A function
                that consumes the IFileLike object whenever the READ event is
                fired.
        """
        raise NotImplementedError()

    @iface.method
    def remove_reader(self, fd: IFileLike) -> bool:
        """Remove a file descriptor waiting for READ from the processor.

        Args:
            fd (IFileLike): Any obect that exposes a 'fileno' method that
                returns a valid file descriptor integer.

        Returns:
            bool: True if the reader was removed. False if it was not in the
                processor.
        """
        raise NotImplementedError()

    @iface.method
    def add_writer(
            self,
            fd: IFileLike,
            callback: typing.Callable[[IFileLike], typing.Any],
    ) -> None:
        """Add a file descriptor to the processor and wait for WRITE.

        Args:
            fd (IFileLike): Any obect that exposes a 'fileno' method that
                returns a valid file descriptor integer.
            callback (typing.Callable[[IFileLike], typing.Any]): A function
                that consumes the IFileLike object whenever the WRITE event is
                fired.
        """
        raise NotImplementedError()

    @iface.method
    def remove_writer(self, fd: IFileLike) -> bool:
        """Remove a file descriptor waiting for WRITE from the processor.

        Args:
            fd (IFileLike): Any obect that exposes a 'fileno' method that
                returns a valid file descriptor integer.

        Returns:
            bool: True if the reader was removed. False if it was not in the
                processor.
        """
        raise NotImplementedError()
