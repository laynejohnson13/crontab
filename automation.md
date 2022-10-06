1. 0 8 * * *  - Every day at 8am

2) 0 22 * * SUN - Every Sunday at 10pm
3) 0 0 1 */3 * - At midnight in every 3rd month

Steps for crontab automation setup

1. Create virtual machine names 'crontab' through GCP
2. sudo apt-get update
3. git clone command
4. cd crontab
5. pwd
6. crontab -e
7. select 1
8. enter in cron jobs & pwd,python.py
9. systemctl status cron
