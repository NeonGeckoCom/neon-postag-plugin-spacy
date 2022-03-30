from ovos_plugin_manager.postag import PosTagger
from ovos_plugin_manager.tokenization import Tokenizer
import spacy


class SpacyPosTagger(PosTagger):
    def __init__(self, config=None):
        super().__init__(config)
        # TODO allow defining your own model
        self.nlp = spacy.load("en_core_web_sm")

    def postag(self, spans, lang=None):
        lang = lang or self.lang
        # TODO multiple models for lang support

        # restore sentence from spans and create a spacy doc
        sentence = Tokenizer.restore_spans(spans)
        doc = self.nlp(sentence)

        return [(token.idx, token.idx + len(token.text), token.text, token.pos_) for token in doc]
