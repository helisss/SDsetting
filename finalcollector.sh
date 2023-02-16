#!/bin/bash

zip -r outputs.zip outputs/

runpodctl send outputs.zip
