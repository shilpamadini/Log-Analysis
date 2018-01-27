# Log-Analysis

This folder contains the necessary program files to generate log analysis report from "news" database.

# Design

This code generates three reports out of "news" database.

1. The database consists of the following tables.
    * authors
        * Table contains name, bio and id (unique id) columns
    * articles
        * Table contains author (foreign key to authors (id)),title,slug,lead,body, time columns
    * log
        * Table contains path,ip,method,status, time and id columns
2. ***The most popular three articles of all time***
    * Data required to generate this report lies in two tables
    articles and logs.
    * The view "title_logs" is created to associate log table data with corresponding article title using values of path column.
    * The data in "title_view" is later aggregated to generate the number of views  for each article and select the top three articles that have the most views.
3. ***The most popular authors of all time***
    * Data in the view "title_logs" is joined with authors table to
    generate the number of views for each author.
4. ***The days when more than 1% of requests lead to errors***
    * The view "log_req_prcnt" is created derive percentage of each request status out of total number of requests received per day.
    * This view is later queried to retrieve the data when more than 1% of the requests lead to errors.

## Contents

1. loganalysis.py
    * Python file containing the database code run the reporting sql against the database.
2. log_req_prcnt.sql
    * sql file to create "log_req_prcnt" view. This view displays the
    aggregates counts HTTP request status per each distinct date and HTTP request method.
3. title_logs.sql
    * sql file to create "title_logs" view. This view displays the log table data in association with article titles and author ids.
4. newsdata.sql
    * sql file to create "news" database and the related tables.

## Installation

1. This project can be run on a Linux-based virtual machine that comes pre-installed with the PostgreSQL database, python and other necessary software.
2. We will use Vagrant and VirtualBox to install and manage this VM.
3. Downloaded VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).Install the platform package
for your operating system. No need to download the extension package or SDK.There is also no need to launch VirtualBox.
4. Download  and setup Vagrant by using the following commands.
    * ```git clone https://github.com/udacity/fullstack-nanodegree-vm```
    * Change to the "fullstack-nanodegree-vm" folder in the terminal.
        * ```cd vagrant```
    * To download and install the Linux OS. Run the following command in vagrant directory.
        * ```vagrant up```
    * Once Vagrant up  finished running run the following command to login to VM
        * ```vagrant ssh```
    * All the files in "vagrant" directory on your terminal will appear in the "/vagrant" directory on the VM
 5. Once you are in the "vagrant" directory
    *
