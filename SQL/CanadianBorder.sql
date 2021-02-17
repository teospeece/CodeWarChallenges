/*
Teo Speece:
kata link: https://www.codewars.com/kata/590ba881fe13cfdcc20001b4/train/sql

Instructions:
Select names, and countries of origin of all the travelers, excluding anyone from Canada, Mexico, or The US.

travelers table schema

name
country

*/

-- Code
select * from travelers
where Country not in ('USA', 'Mexico', 'Canada')