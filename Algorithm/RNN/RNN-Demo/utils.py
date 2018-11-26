import torch
import torch.nn.functional as F
import numpy as np
import math

word2idx  =  torch.load('../../data/PTB/data/word2idx.pt')
idx2word  =  torch.load('../../data/PTB/data/idx2word.pt')

def normalize_gradient(net):

    grad_norm_sq=0

    for p in net.parameters():
        grad_norm_sq += p.grad.data.norm()**2

    grad_norm=math.sqrt(grad_norm_sq)

    if grad_norm<1e-4:
        net.zero_grad()
        print('grad norm close to zero')
    else:
        for p in net.parameters():
             p.grad.data.div_(grad_norm)

    return grad_norm


def display_num_param(net):
    nb_param = 0
    for param in net.parameters():
        nb_param += param.numel()
    print('There are {} ({:.2f} million) parameters in this neural network'.format(
        nb_param, nb_param/1e6)
         )

def sentence2vector(sentence):
    words = sentence.split()
    x = torch.LongTensor(len(words),1)
    for idx, word in enumerate(words):

         if word not in word2idx:
            print('You entered a word which is not in the vocabulary.')
            print('Make sure that you do not have any capital letters')
         else:
            x[idx,0]=word2idx[word]
    return x


def show_next_word(scores):
    num_word_display=30
    prob=F.softmax(scores,dim=2)
    p=prob[-1].squeeze()
    p,word_idx = torch.topk(p,num_word_display)

    for i,idx in enumerate(word_idx):
        percentage= p[i].item()*100
        word=  idx2word[idx.item()]
        print(  "{:.1f}%\t".format(percentage),  word )
