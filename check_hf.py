from huggingface_hub import HfApi, hf_hub_download, snapshot_download, Repository
api = HfApi(token = "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")
#api.create_repo(repo_id="test_push")
repo = Repository(local_dir = "./")
repo.git_pull()
repo.push_to_hub(commit_message = "test1")
