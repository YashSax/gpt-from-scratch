## General Description

A from-scratch implementation of a decoder-only transformer model using Pytorch for Shakespearian text generator. This model is trained on the tiny_shakespeare dataset, containing ~40,000 lines of text from the plays of Shakespeare. The transformer implementation was created following Andrej Karpathy's "Build GPT from Scratch" tutorial here: https://www.youtube.com/watch?v=kCc8FmEb1nY&list=WL&index=30&t=4s&ab_channel=AndrejKarpathy

The model implemented in the tutorial is a character-based model, but in this project I decided to implement the WordPiece tokenizer algorithm, as described here: https://www.youtube.com/watch?v=qpv6ms_t_1A&ab_channel=HuggingFace

## Files

`train.ipynb` : The main file that defines and trains the transformer


`tokenizer.ipynb` : Contains code used for training the tokenizer


`tokenizer_tokens` : Contains a list of the learned tokens


`tokenizer.py` : Contains the `Tokenizer` class, which can take an input of a list of tokens and can tokenize arbitrary text

`input.txt` : the tiny_shakespeare dataset

## Usage

Install pytorch here: https://pytorch.org/get-started/locally/
The only other two external libraries needed are `tqdm` and `re`, which can be installed as follows:

```
pip install tqdm
pip install regex
```

Train the tokenizer by running `tokenizer.ipynb`. The learned tokens will be saved in `tokenizer_tokens`. Then run `train.ipynb`, which will load those tokens and train on the dataset in `input.txt`.