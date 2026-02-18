from __future__ import annotations

import sys

from pse2.ui.cli import run_cli
from pse2.ui.qt_app import run_qt


def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "cli":
        sys.argv.pop(1)
        run_cli()
    else:
        if len(sys.argv) > 1 and sys.argv[1].lower() == "gui":
            sys.argv.pop(1)
        run_qt()


if __name__ == "__main__":
    main()
