#!/bin/bash

#huggingface-cli login

#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
apt update

apt isntall vim

apt install 
git clone https://huggingface.co/ENSEONG/selfmix

# Make sure you have git-lfs installed
# (https://git-lfs.github.com/)
#git lfs install

cp -r selfmix/setmodel/models/Lora ./models
cp -r selfmix/setmodel/models/Stable-diffusion ./models
cp -r selfmix/setmodel/models/VAE ./models
cp -r selfmix/setmodel/embeddings ./

#git add . && git commit -m "Update from $USER"
#git push
