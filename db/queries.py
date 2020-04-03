# Pokemon
get_pokemon_by_id = "select pokemon_species.id, pokemon_species_names.name, pokemon.height, pokemon.weight, pokemon.base_experience, pokemon.'order', pokemon.is_default, pokemon_species.gender_rate, pokemon_species_names.genus from pokemon_species join pokemon_species_names on pokemon_species.id = pokemon_species_names.pokemon_species_id join pokemon on pokemon_species.id = pokemon.species_id where pokemon_species.id = %d and pokemon_species_names.local_language_id = %d"
get_types_by_pokemon = "select pokemon_types.type_id as id, pokemon_types.slot, type_names.name from pokemon_types join type_names on pokemon_types.type_id = type_names.type_id where pokemon_types.pokemon_id = %d and type_names.local_language_id = %d"
get_moves_by_pokemon = "select pokemon_moves.move_id as id, pokemon_moves.pokemon_move_method_id, pokemon_moves.level, machines.machine_number, move_names.name, moves.type_id from pokemon_moves join move_names on pokemon_moves.move_id = move_names.move_id join moves on pokemon_moves.move_id = moves.id left outer join (select * from machines where machines.version_group_id = %d) as machines on pokemon_moves.move_id = machines.move_id where pokemon_moves.pokemon_id = %d and pokemon_moves.version_group_id = %d and move_names.local_language_id = %d order by pokemon_moves.pokemon_move_method_id asc, pokemon_moves.level asc, machines.machine_number asc"