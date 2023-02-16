#!/bin/bash

#huggingface-cli login

#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

git clone https://huggingface.co/ENSEONG/selfmix

# Make sure you have git-lfs installed
# (https://git-lfs.github.com/)
git lfs install

cp -r selfmix/setmodel/models/Lora ./models/Lora
cp -r selfmix/setmodel/models/Stable-diffusion ./models/Stable-diffusion
cp -r selfmix/setmodel/models/VAE ./models/VAE
cp -r selfmix/setmodel/embeddings ./embeddings

#git add . && git commit -m "Update from $USER"
#git push
