# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2011 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##
"""Test pyflakes on stoq, stoqlib and plugins directories

Useful to early find syntax errors and other common problems.
"""
import unittest

import pep8

from testutils import SourceTest

ERRORS = (
    'E501',  # line too long
)


class TestPEP8(SourceTest, unittest.TestCase):

    def check_filename(self, root, filename):
        pep8style = pep8.StyleGuide(parse_argv=False, config_file=True)
        pep8style.options.ignore = ERRORS
        report = pep8style.input_file(filename)
        if report:
            raise AssertionError(
                "ERROR: %d PEP8 errors in %s" % (report, filename, ))

suite = unittest.TestLoader().loadTestsFromTestCase(TestPEP8)

if __name__ == '__main__':
    unittest.main()
