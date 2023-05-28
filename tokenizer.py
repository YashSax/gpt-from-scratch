import re
import json

class Tokenizer:
    def __init__(self, vocab_path):
        self.token_to_idx, self.idx_to_token = self.get_mapping(vocab_path)
    
    def get_mapping(self, filepath):
        with open(filepath, 'r') as f:
            vocab = json.load(f)
        self._vocab = vocab
        token_to_idx = {val : idx for idx, val in enumerate(vocab)}
        idx_to_token = {idx : val for idx, val in enumerate(vocab)}

        token_to_idx[" "] = len(vocab)
        idx_to_token[len(vocab)] = " "

        token_to_idx["\n"] = len(vocab) + 1
        idx_to_token[len(vocab) + 1] = "\n"

        return token_to_idx, idx_to_token

    def encode(self, s):
        s = s.strip()
        tokenized = []
        split_sent = re.split("([ \n])", s)
        sent_iter = iter(split_sent)
        for i in sent_iter:
            tokenized.extend(self.tokenize(i))
            if i is not split_sent[-1]:
                tokenized.append(next(sent_iter))
        return [self.token_to_idx[i] for i in tokenized]

    def tokenize(self, word):
        tokenized = []
        ptr = 0

        while ptr < len(word):
            remaining_word = word[ptr:]

            for i in range(len(remaining_word), 0, -1):
                subword = remaining_word[:i]
                found = False
                for token in self._vocab:
                    if self.token_equality(token, ptr, subword):
                        tokenized.append(token)
                        ptr += len(subword)
                        found = True
                        break
                if found:
                    break
        return tokenized
    
    def token_equality(self, token, index, subword):
        if not self.get_word_from_token(token) == subword:
            return False
        if index == 0 and token[0] == "#":
            return False
        if index != 0 and token[0] != "#":
            return False
        return True

    def get_word_from_token(self, token):
        if token[0] == "#":
            return token[2:]
        return token

    def decode(self, s):
        raw_tokens = [self.get_word_from_token(self.idx_to_token[i]) for i in s]
        return ''.join(raw_tokens)
        