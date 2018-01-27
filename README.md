# Log-Analysis

This folder contains the necessary program files to generate log analysis reports from "news" database.

## Contents

1. loganalysis.py
    * Python file containing the database code to run the reports.
2. log_req_prcnt.sql
    * sql file to create "log_req_prcnt" view.
3. title_logs.sql
    * sql file to create "title_logs" view.

## Installation

This project can be run on a Linux-based virtual machine that comes pre-installed with the PostgreSQL database, python and other necessary software.

1. Download the following software to run the project.
    * Download VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).Install the platform package for your operating system. No need to download the extension package or SDK.There is also no need to launch VirtualBox.
    * Download "Vagrant" from the following git repository.
        * ```git clone https://github.com/udacity/fullstack-nanodegree-vm```
    * On your Terminal navigate to  "fullstack-nanodegree-vm" folder cloned from the above GIT repository. Navigate to vagrant subdirectory.
        * ```cd vagrant```
    * Download the data for the  news database [here] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Verify "newsdata.sql" is downloaded to "vagrant" directory
    * Use the following command to clone the project repository.
        * ```git clone https://github.com/shilpamadini/Log-Analysis.git```
3. Run the following commands to install the required software.
    * Navigate to the "vagrant" directory where above mentioned software is downloaded.
    * To install the Linux VM. Run the following command.
        * ```vagrant up```
    * Once Vagrant up is finished running,run the following command to login to VM
        * ```vagrant ssh```
    * All the files in "vagrant" directory on your terminal will appear in the "/vagrant" directory on the VM
    *  At the VM shell prompt
        * ```cd /vagrant```
        * ```psql -d news -f newsdata.sql```
    * At the psql prompt please run following to create required views.
        * ```create view title_logs as
    (select ar.author,ar.title,ar.slug,lg.path,lg.ip,lg.method,lg.status,lg.time,lg.id from articles ar , log lg
    where lg.path like '%'||ar.slug||'%' order by ar.title);```
        * ```create view log_req_prcnt as
    (
    select s.date,s.method,s.status,
    s.cnt_status,r.cnt_requests,(s.cnt_status * 100)::numeric/r.cnt_requests as percentage
    from
    (select method,status,time::date as date, count(status) as cnt_status
    from log group by method,status,date order by date) s,
    (select method,time::date as date ,count(method) as cnt_requests
    from log group by method, date order by date) r
    where s.method = r.method
    and s.date = r.date
    order by s.date
    );```
        * ```\q``` to go back to shell prompt
    * At the VM shell prompt run the python script to generate reports.
        * ```python loganalysis.py```
