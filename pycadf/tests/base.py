# -*- encoding: utf-8 -*-
#
# Copyright 2013 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Test base classes.
"""
import os.path
from oslo.config import cfg
import testtools


class TestCase(testtools.TestCase):

    def setUp(self):
        super(TestCase, self).setUp()
        cfg.CONF([], project='pycadf')

    def path_get(self, project_file=None):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            '..',
                                            '..',
                                            )
                               )
        if project_file:
            return os.path.join(root, project_file)
        else:
            return root

    def tearDown(self):
        cfg.CONF.reset()
        super(TestCase, self).tearDown()
