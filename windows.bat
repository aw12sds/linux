

=mysql备份
@echo off
set "Ymd=%date:~,4%%date:~5,2%%date:~8,2%"
"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump" --skip-extended-insert -u root --password=root zkxj_erp_new> E:\db_backup\performance_%Ymd%.sql
@echo on



=删除回收站
echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin"
