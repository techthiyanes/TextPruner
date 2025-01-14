from . import  model_utils
from . import tokenizer_utils

MODEL_MAP = {
    'albert': 
        {'resizer': model_utils.AlbertVocabResizer,
         'tokenizer_helper': tokenizer_utils.SentencepieceTokenizer,
         'structure': model_utils.AlbertStructure},
    'bert':
        {'resizer': model_utils.BertVocabResizer,
         'tokenizer_helper': tokenizer_utils.SubwordTokenizer,
         'structure': model_utils.BertStructure},
    'electra': 
        {'resizer': model_utils.ElectraVocabResizer,
         'tokenizer_helper': tokenizer_utils.SubwordTokenizer,
         'structure': model_utils.ElectraStructure},
    'roberta':
        {'resizer': model_utils.RobertaVocabResizer,
          'tokenizer_helper' : tokenizer_utils.RobertaGPT2Tokenizer,
          'structure': model_utils.RobertaStructure},
    'xlm-roberta':
        {'resizer':model_utils.XLMRobertaVocabResizer,
          'tokenizer_helper': tokenizer_utils.XLMRSentencepieceTokenizer,
          'structure': model_utils.XLMRobertaStructure}
}