import unittest
from quebra_frases import span_indexed_word_tokenize
from neon_postag_plugin_spacy import SpacyPosTagger


class TestSpacyPosTagger(unittest.TestCase):

    def test_postag(self):
        solver = SpacyPosTagger()
        tokens = span_indexed_word_tokenize("Once upon a time there was a free and open voice assistant")
        self.assertEqual(solver.postag(tokens),
                         [(0, 4, 'Once', 'ADV'),
                          (5, 9, 'upon', 'SCONJ'),
                          (10, 11, 'a', 'DET'),
                          (12, 16, 'time', 'NOUN'),
                          (17, 22, 'there', 'PRON'),
                          (23, 26, 'was', 'AUX'),
                          (27, 28, 'a', 'DET'),
                          (29, 33, 'free', 'ADJ'),
                          (34, 37, 'and', 'CCONJ'),
                          (38, 42, 'open', 'ADJ'),
                          (43, 48, 'voice', 'NOUN'),
                          (49, 58, 'assistant', 'NOUN')])

