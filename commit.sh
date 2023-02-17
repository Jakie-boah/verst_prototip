#!/usr/bin/env bash
#datetime_now=`date +'%Y-%m-%d %H:%M:%S'`
git config --global user.name 'NAME'
git config --global user.email 'VanoGalen@yandex.ru'
git add *
git commit -m "admin_panel updated with full-contacts system"
git branch -M main
git remote add origin https://github.com/Jakie-boah/verst_prototip.git
git push -u origin main

