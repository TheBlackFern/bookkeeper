"""
Utilitary fucntions
"""

from typing import Iterable, Iterator


def _get_indent(line: str) -> int:
    return len(line) - len(line.lstrip())


def _lines_with_indent(lines: Iterable[str]) -> Iterator[tuple[int, str]]:
    for line in lines:
        if not line or line.isspace():
            continue
        yield _get_indent(line), line.strip()


def read_tree(lines: Iterable[str]) -> list[tuple[str, str | None]]:
    """
    Read a tree structure from text based on indentation. Return a topologically
    sorted list of pairs "child-parent". For the top level entries parent is None.

    Example. This text:
    parent
        child1
            child2
        child3

    would result in this tree:
    [('parent', None), ('child1', 'parent'),
     ('child2', 'child1'), ('child3', 'parent')]

    Empty lines are ignored

    Parameters
    ----------
    lines - An iterable object that contains lines of text (a file or a list of str)

    Returns
    -------
    "Child-parent" pairs list
    """
    parents: list[tuple[str | None, int]] = []
    last_indent = -1
    last_name = None
    result: list[tuple[str, str | None]] = []
    for i, (indent, name) in enumerate(_lines_with_indent(lines)):
        if indent > last_indent:
            parents.append((last_name, last_indent))
        elif indent < last_indent:
            while indent < last_indent:
                _, last_indent = parents.pop()
            if indent != last_indent:
                raise IndentationError(
                    f"unindent does not match any outer indentation"
                    f"level in line {i}:\n"
                )
        result.append((name, parents[-1][0]))
        last_name = name
        last_indent = indent
    return result
