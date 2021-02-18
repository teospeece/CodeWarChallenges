/*
Teo Speece:
kata link: https://www.codewars.com/kata/5ab828bcedbcfc65ea000099/train/sql

Instructions: Using the following tables, return the pokemon_name, modifiedStrength and element of the Pokemon whose strength, after taking these changes into account, is greater than or equal to 40, ordered from strongest to weakest.

pokemon schema

id
pokemon_name
element_id
str
multipliers schema

id
element
multiplier
*/

-- SQL

select pokemon.pokemon_name, pokemon.str*multipliers.multiplier as modifiedstrength, multipliers.element
from pokemon
full outer join multipliers on pokemon.element_id = multipliers.id
where pokemon.str*multipliers.multiplier >= 40
order by modifiedstrength desc