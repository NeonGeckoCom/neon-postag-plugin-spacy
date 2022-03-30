import unittest
from quebra_frases import span_indexed_word_tokenize
from neon_postag_plugin_spacy import SpacyPosTagger


class TestSpacyPosTagger(unittest.TestCase):

    def test_postag(self):
        solver = SpacyPosTagger()
        tokens = span_indexed_word_tokenize("Once upon a time there was a free and open voice assistant")
        self.assertEqual(solver.postag(tokens),
                         [('Once', 'ADV'),
                          ('upon', 'SCONJ'),
                          ('a', 'DET'),
                          ('time', 'NOUN'),
                          ('there', 'PRON'),
                          ('was', 'AUX'),
                          ('a', 'DET'),
                          ('free', 'ADJ'),
                          ('and', 'CCONJ'),
                          ('open', 'ADJ'),
                          ('voice', 'NOUN'),
                          ('assistant', 'NOUN')])

