import os
import json
import shutil
import wget
import argparse
import git

home_dir = os.getcwd() # get current working directory

# Define a function to set the command line arguments
def argsset():
    parser = argparse.ArgumentParser(description='Select the download type')
    parser.add_argument('--set', action="store_true", help='Turn on setting')
    parser.add_argument('--ext', action="store_true", help='Check extension')
    parser.add_argument('--chconfig', action="store_true", help='Modify ui-config.json file')
    parser.add_argument('--bkconfig', action="store_true", help='Backup ui-config.json file')
    parser.add_argument('--model', action="store_true",  help='Download model type')
    parser.add_argument('--lora', action="store_true",  help='Download model type')
    parser.add_argument('--emb', action="store_true",  help='Download model type')
    # parser.add_argument('--url', required=False, type=str, help='Download model url')
    args = parser.parse_args()
    return args

# Define a function to download models from the urls list
def model_downloader(model_urls, model_type):
    if model_type == 'SD':
        address = 'models/Stable-diffusion'
    elif model_type == 'Lora':
        address = 'models/Lora'
    elif model_type == 'VAE':
        address = 'models/VAE'
    elif model_type == 'emb':
        address = 'embeddings'
    elif model_type == 'controlnet':
        address = 'extensions/sd-webui-controlnet/models'
    
    models_dir = os.path.join(home_dir, address) # create directory to save models
    os.makedirs(models_dir, exist_ok=True) # create directory if it doesn't exist
    for url in model_urls:
        fname = url.split('/')[-1]
        print(f'\n{fname} model file download start')
        wget.download(url, models_dir)



# Define a function to download extensions from the urls list
def ext_downloader(urls):
    ext_dir = os.path.join(home_dir, 'extensions') # create directory to save extensions
    os.makedirs(ext_dir, exist_ok=True) # create directory if it doesn't exist
    for url in urls:
        # os.system(git clone {url} ext_dir)
        git.Git(ext_dir).clone(url)

# Define a function to set default prompt
def set_default_prompt(positive, negative):
    # Backup ui-config.json file
    ui_conf_path = os.path.join(home_dir, 'ui-config.json')
    ui_conf_bk_path = os.path.join(home_dir, 'ui-config_bk.json')
    if not os.path.exists(ui_conf_bk_path):
        shutil.copy(ui_conf_path, ui_conf_bk_path)
    with open(ui_conf_path, 'r', encoding='utf-8') as f:
        orig_ui = json.load(f)
        ur_ui = orig_ui

    # Modify ui-config.json file
    ur_ui['txt2img/Prompt/value'] = positive
    ur_ui['txt2img/Negative prompt/value'] = negative

    ur_ui['img2img/Prompt/value'] = positive
    ur_ui['img2img/Negative prompt/value'] = negative

    # Save changes to ui-config.json file
    with open(ui_conf_path, 'w', encoding='utf-8') as f:
        json.dump(ur_ui, f, indent=4)

def clean_modelconfig():

    conf_path = os.path.join(home_dir, 'config.json')
    conf_bk_path = os.path.join(home_dir, 'config_bk.json')
    if not os.path.exists(conf_bk_path):
        shutil.copy(conf_path, conf_bk_path)
    with open(conf_path, 'r', encoding='utf-8') as f:
        orig_conf = json.load(f)
        ur_conf = orig_conf

    # Modify config.json file
    ur_conf['sd_checkpoint_hash'] = ""
    ur_conf['sd_model_checkpoint'] = ""

    # Save changes to config.json file
    with open(conf_path, 'w', encoding='utf-8') as f:
        json.dump(ur_conf, f, indent=4)

# Define a function to backup ui-config.json file
def backup_config():
    try:
        ui_conf_path = os.path.join(home_dir, 'ui-config.json')
        ui_conf_bk_path = os.path.join(home_dir, 'ui-config_bk.json')

        shutil.copy(ui_conf_bk_path, ui_conf_path)

    except:
        print("There is no backup config file")


if __name__ == '__main__':
    args = argsset()
    with open("SDsetting/defaultset.json", 'r', encoding='utf-8') as reader:
        default = json.load(reader)
        
    if args.set:
        ext_downloader(default["extensions"])
                
        model_downloader(default["model_urls"], "SD")
        model_downloader(default["lora_urls"], "Lora")
        model_downloader(default["vae_urls"], "VAE")
        model_downloader(default["emb_urls"], "emb")
        model_downloader(default["contorlnet_urls"], "controlnet")
                
        set_default_prompt(default["positive"],default["negative"])
        #clean_modelconfig()
        
    elif args.ext:
        # model_url = input("Enter the urls:   ")
        # model_urls = [model_url]
        # ext_downloader(model_urls)
        ext_downloader(default["extensions"])
        
    elif args.chconfig:
        positive = input("Enter the Positive default prompt :   ")
        negative = input("Enter the Negative default prompt :   ")
        set_default_prompt(positive,negative)
        
    elif args.bkconfig:
        backup_config()
    
    else:
        print("#"*5,"Downlaod Models from URL","#"*5)
        print()
        model_type = input("Enter the Model Type(SD, Lora, VAE, emb):   ")
        model_url = input("Enter the urls:   ")
        model_urls = [model_url]
        model_downloader(model_urls,model_type)
        
    
    
