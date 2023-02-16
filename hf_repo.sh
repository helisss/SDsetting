#!/bin/bash

huggingface-cli login

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

git clone https://huggingface.co/ENSEONG/selfmix

# Make sure you have git-lfs installed
# (https://git-lfs.github.com/)
git lfs install

cp selfmix/setmodel/models/Lora models/Lora
cp selfmix/setmodel/models/Stable-diffusion models/Stable-diffusion
cp selfmix/setmodel/models/VAE models/VAE
cp selfmix/setmodel/embeddings /embeddings

#git add . && git commit -m "Update from $USER"
#git push
