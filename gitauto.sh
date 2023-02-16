#!/bin/bash
REMOTE_REPO=$(git remote)
WORKING_BRANCH=$(git branch --show-current)

git pull ${REMOTE_REPO} ${WORKING_BRANCH}

echo "> pull complete from remote:${REMOTE_REPO} branch:${WORKING_BRANCH}"

git add .

echo "> add all files"

if [ $# -eq 0 ]; then
  read -p "> enter commit message : " COMMIT_MESSAGE
else 
  COMMIT_MESSAGE=${1}
fi

git commit -m "${COMMIT_MESSAGE}"

echo "> commit complte"

git push ${REMOTE_REPO} HEAD:${WORKING_BRANCH}

if [ $? = 0 ]; then
  echo "> push complete to remote:${REMOTE_REPO} branch:${WORKING_BRANCH}"
else
  git reset --soft HEAD^
  echo "> push faild. please check the git error message."
fi

# 주의 : REMOTE_REPO 에 모든 remote 이름이 저장되기 때문에,
# remote가 여러 개 연결되어 있을 시 의도한 대로 작동하지 않을 수 있습니다.
