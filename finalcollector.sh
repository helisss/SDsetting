#!/bin/bash

zip -r /workspace/outputs.zip /workspace/outputs

runpodctl send outputs.zip
