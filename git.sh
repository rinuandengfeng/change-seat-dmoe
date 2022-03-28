#!/bin/bash
echo "================="
echo "auto git by JOEY"
echo "======= 🤪  ========="

echo -e  "
▶ \033[33;1mgit add .
\033[0m"
git add .

git status
echo -e "
▶ \033[33;1mcommit message:
\033[37;1m"


echo -e "
dime = $(date -d + %Y%m%d)
▶ \033[33;1mgit commit -m 'date'
\033[0m"
git commit -m "auto push at $date"

echo -e "
▶ \033[33;1mgit push
"
echo -e "\033[37;1mstart pushing ...\033[0m
"
git push
echo -e "
\033[37;1mAll Done\033[0m"