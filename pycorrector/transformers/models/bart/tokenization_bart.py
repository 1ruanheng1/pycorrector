# coding=utf-8
# Copyright 2020 The Facebook AI Research Team Authors and The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, Optional

from ..roberta.tokenization_roberta import RobertaTokenizer
from ...tokenization_utils_base import BatchEncoding

# vocab and merges same as roberta
vocab_url = "https://huggingface.co/roberta-large/resolve/main/vocab.json"
merges_url = "https://huggingface.co/roberta-large/resolve/main/merges.txt"
_all_bart_models = [
    "facebook/bart-base",
    "facebook/bart-large",
    "facebook/bart-large-mnli",
    "facebook/bart-large-cnn",
    "facebook/bart-large-xsum",
    "yjernite/bart_eli5",
    # This is not exhaustive: see https://huggingface.co/models?filter=bart
]


class BartTokenizer(RobertaTokenizer):
    r"""
    Construct a BART tokenizer.

    :class:`~transformers.BartTokenizer` is identical to :class:`~transformers.RobertaTokenizer` and adds a new
    :meth:`~transformers.BartTokenizer.prepare_seq2seq_batch`

    Refer to superclass :class:`~transformers.RobertaTokenizer` for usage examples and documentation concerning the
    initialization parameters and other methods.
    """
    # merges and vocab same as Roberta
    max_model_input_sizes = {m: 1024 for m in _all_bart_models}
    pretrained_vocab_files_map = {
        "vocab_file": {m: vocab_url for m in _all_bart_models},
        "merges_file": {m: merges_url for m in _all_bart_models},
    }

    def prepare_seq2seq_batch(
            self,
            src_texts: List[str],
            tgt_texts: Optional[List[str]] = None,
            max_length: Optional[int] = None,
            max_target_length: Optional[int] = None,
            padding: str = "longest",
            return_tensors: str = None,
            truncation=True,
            **kwargs,
    ) -> BatchEncoding:
        kwargs.pop("src_lang", None)
        kwargs.pop("tgt_lang", None)
        if max_length is None:
            max_length = self.model_max_length
        model_inputs: BatchEncoding = self(
            src_texts,
            add_special_tokens=True,
            return_tensors=return_tensors,
            max_length=max_length,
            padding=padding,
            truncation=truncation,
            **kwargs,
        )
        if tgt_texts is None:
            return model_inputs
        # Process tgt_texts
        if max_target_length is None:
            max_target_length = max_length
        labels = self(
            tgt_texts,
            add_special_tokens=True,
            return_tensors=return_tensors,
            padding=padding,
            max_length=max_target_length,
            truncation=truncation,
            **kwargs,
        )["input_ids"]
        model_inputs["labels"] = labels
        return model_inputs
