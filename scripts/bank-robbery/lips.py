#!/usr/bin/env python3
"""Moved to scripts/lipsync/lips.py (2026-10-29). This shim keeps old commands working
(build-short7.py runs `<this folder>/lips.py <clip>`, and the docs quote this path)."""
import os, runpy, sys

REAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lipsync', 'lips.py')
if __name__ == '__main__':
    sys.argv[0] = REAL
    runpy.run_path(REAL, run_name='__main__')
else:
    import importlib.util
    _spec = importlib.util.spec_from_file_location('_lipsync_lips', REAL)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    globals().update({k: v for k, v in vars(_mod).items() if not k.startswith('__')})
