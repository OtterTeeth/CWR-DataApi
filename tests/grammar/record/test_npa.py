# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.record import nra


"""
CWR Non-Roman Alphabet Agreement Party Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPAGrammar(unittest.TestCase):
    """
    Tests that the NPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = nra.npa

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('012345678', result.ip_id)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual('ES', result.language)

    def test_valid_min(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'NPA0000123400000023000000000PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                                 '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('000000000', result.ip_id)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual(None, result.language)