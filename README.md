scusage
=====================================================
![PyPI version](https://img.shields.io/pypi/v/scusage)
[![CodeQL](https://github.com/tobi-wan-kenobi/scusage/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/tobi-wan-kenobi/scusage/actions/workflows/codeql-analysis.yml)
![License](https://img.shields.io/github/license/tobi-wan-kenobi/scusage)

`scusage` is a small tool to analyze your keyboard shortcut usage (hence the name -
**S**hort**C**ut **usage**) to help you find optimal keybindings.

Currently, it only supports the i3 window manager.

# Installation

```
$ pip install --user scusage
```

# Usage

```
$ ./bin/scusage -h
usage: scusage [-h] [--file FILE] [--resume]

monitor and report i3 keyboard shortcut usage

options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  file for reading and writing usage data. if not specified, no data will be written.
  --resume              if provided, data is appended to <FILE>. otherwise, <FILE> is overwritten
```

If you run `scusage` without parameters, you simply use your window manager, and
when you want to get the results, you terminate `scusage` using `Ctrl+C`:

```
$ scusage
# let scusage run while you go about your daily business
# when you are done, terminate the tool with Ctrl+C

shortcut                                                                          count
--------------------------------------------------------------------------------  -------  ------------------------------
Mod4+2: workspace "2: "                                                           7 (22%)  ==============================
Mod4+3: workspace "3: "                                                           7 (22%)  ==============================
Mod4+4: workspace "4: "                                                           5 (16%)  =====================
Mod4+5: workspace "5: "                                                           3 (9%)   ============
Mod4+r: exec "rofi -modi window,drun,ssh,combi -show combi"                       3 (9%)   ============
Mod4+1: workspace "1: "                                                           2 (6%)   ========
Mod4+s: mark swapee; focus right; swap container with mark swapee; unmark swapee  2 (6%)   ========
Mod4+8: workspace "8:  "                                                          1 (3%)   ====
Mod4+9: workspace "9: "                                                           1 (3%)   ====
Mod4+0: workspace "10: "                                                          1 (3%)   ====
```

The idea is that this tool helps you identify which shortcuts you use most often,
so that you can bind them to convenient and easy to reach key combinations.

For collecting data across window manager sessions, you can use `--file`
and `--resume` to store and load usage data from a file.
