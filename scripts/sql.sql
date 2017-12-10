create database pybackenddb;

use pybackenddb;

create user 'pybackend'@'localhost'
identified by 'pybackend';

grant create, insert, select, update, delete on pybackenddb.* to 'pybackend'@'localhost';
