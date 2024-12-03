import re

# Correct order of table inserts
table_order = [
    "TimeZone",
    "Venue",
    "TeamName",
    "player_info",
    "OfficialInfo",
    "team_info",
    "game",
    "Event",
    "Officiates",
    "game_skater_stats",
    "game_goalie_stats",
    "game_scratches",
    "game_teams_stats",
    "game_goals",
    "game_penalties",
    "Performs"
]

# Function to parse INSERT statements by table name
def parse_insert_statements(sql_content):
    insert_statements = {}
    for table in table_order:
        insert_statements[table] = []
    
    # Regex to capture INSERT INTO statements
    pattern = re.compile(r"INSERT INTO (\w+)\s+VALUES", re.IGNORECASE)
    lines = sql_content.splitlines()
    for line in lines:
        match = pattern.match(line)
        if match:
            table_name = match.group(1)
            if table_name in insert_statements:
                insert_statements[table_name].append(line)
    return insert_statements

# Function to write the sorted INSERT statements to a file
def write_sorted_inserts(insert_statements, output_file):
    with open(output_file, "w") as f:
        for table in table_order:
            if insert_statements[table]:
                f.write(f"-- Inserts for {table} --\n")
                for statement in insert_statements[table]:
                    f.write(statement + "\n")
                f.write("\n")

# Main logic
def rearrange_insert_statements(input_file, output_file):
    with open(input_file, "r") as f:
        sql_content = f.read()
    
    insert_statements = parse_insert_statements(sql_content)
    write_sorted_inserts(insert_statements, output_file)

# Input and output files
input_sql_file = "cleaned_output.sql"
output_sql_file = "sorted_nhl.sql"

# Run the script
rearrange_insert_statements(input_sql_file, output_sql_file)
print(f"Sorted INSERT statements have been written to {output_sql_file}")
