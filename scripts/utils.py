# utils.py

import pandas as pd

def break_up_pidms(input_csv, output_txt):
    """
    Reads a CSV file containing PIDMs, formats them as 7-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    with the first section as "pidm IN (...)" and subsequent sections as "OR pidm IN (...)".

    :param input_csv: Path to the CSV file containing PIDMs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=0, names=['PIDM'])  # Skip header row
    df['PIDM'] = df['PIDM'].astype(str).str.zfill(7)

    pidm_groups = [df['PIDM'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []

    for idx, group in enumerate(pidm_groups):
        formatted_pidms = [f"'{pidm}'" for pidm in group[:-1]] + [group[-1]] if len(group) > 1 else [group[0]]

        if idx == 0:
            sql_query = f"pidm IN ({', '.join(formatted_pidms)})"
        else:
            sql_query = f"OR pidm IN ({', '.join(formatted_pidms)})"
        
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))

    print(f"✅ Export successful! File saved to: {output_txt}")

def break_up_whkeys(input_csv, output_txt):
    """
    Reads a CSV file containing WHKEYs, formats them as 9-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    with the first section as "whkey IN (...)" and subsequent sections as "OR whkey IN (...)".

    :param input_csv: Path to the CSV file containing WHKEYs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=0, names=['WHKEY'])  # Skip header row
    df['WHKEY'] = df['WHKEY'].astype(str).str.zfill(9)

    whkey_groups = [df['WHKEY'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []

    for idx, group in enumerate(whkey_groups):
        formatted_whkeys = [f"'{whkey}'" for whkey in group[:-1]] + [group[-1]] if len(group) > 1 else [group[0]]

        if idx == 0:
            sql_query = f"whkey IN ({', '.join(formatted_whkeys)})"
        else:
            sql_query = f"OR whkey IN ({', '.join(formatted_whkeys)})"
        
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))

    print(f"✅ Export successful! File saved to: {output_txt}")

def break_up_pantherids(input_csv, output_txt):
    """
    Reads a CSV file containing PantherIDs, formats them as 9-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    with the first section as "pantherid IN (...)" and subsequent sections as "OR pantherid IN (...)".

    :param input_csv: Path to the CSV file containing PantherIDs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=0, names=['PANTHERID'])  # Skip header row
    df['PANTHERID'] = df['PANTHERID'].astype(str).str.zfill(9)

    pantherid_groups = [df['PANTHERID'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []

    for idx, group in enumerate(pantherid_groups):
        formatted_pantherids = [f"'{pantherid}'" for pantherid in group[:-1]] + [group[-1]] if len(group) > 1 else [group[0]]

        if idx == 0:
            sql_query = f"pantherid IN ({', '.join(formatted_pantherids)})"
        else:
            sql_query = f"OR pantherid IN ({', '.join(formatted_pantherids)})"
        
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))

    print(f"✅ Export successful! File saved to: {output_txt}")
