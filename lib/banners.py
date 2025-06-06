#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module just prints an ASCII logo and banners."""

# Standard Libraries
import random
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding='utf-8')
    else:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
except Exception:
    pass

def print_banner():
    """Just a function to print sweet ASCII art banners."""
    banner_1 = ("""
 ██████╗  ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██║  ███╗██║   ██║██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║
██║   ██║██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║
╚██████╔╝╚██████╔╝██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝
 for GoPhish -- getgophish.com
 """)

    banner_2 = ("""
  #####         ######
 #     #  ####  #     # ###### #####   ####  #####  #####
 #       #    # #     # #      #    # #    # #    #   #
 #  #### #    # ######  #####  #    # #    # #    #   #
 #     # #    # #   #   #      #####  #    # #####    #
 #     # #    # #    #  #      #      #    # #   #    #
  #####   ####  #     # ###### #       ####  #    #   #
for GoPhish -- getgophish.com
""")

    banner_3 = ("""
   _|_|_|            _|_|_|                                              _|
 _|          _|_|    _|    _|    _|_|    _|_|_|      _|_|    _|  _|_|  _|_|_|_|
 _|  _|_|  _|    _|  _|_|_|    _|_|_|_|  _|    _|  _|    _|  _|_|        _|
 _|    _|  _|    _|  _|    _|  _|        _|    _|  _|    _|  _|          _|
   _|_|_|    _|_|    _|    _|    _|_|_|  _|_|_|      _|_|    _|            _|_|
                                         _|
 for GoPhish -- getgophish.com           _|
""")

    logo = ("""
                     ```
                ```````````
             `````       `````
         `````              ``````
      `````                     `````
    ```                ` `         ````
    ```                 `           ```
    ```                 `           ```
    ```                 `           ```
    ```                 `           ```
    ```         `       `           ```
    ```         `       `           ```
    ```         `       `           ```
    ```          `     `            ```
    ```             `               ```
      `````                     `````
         `````               `````
             `````       `````
                ````` `````
                    ```""")

    art = [banner_1, banner_2, banner_3]

    try:
        print(logo)
        print(random.choice(art))
    except UnicodeEncodeError:
        print("Banner could not be displayed due to encoding.")
