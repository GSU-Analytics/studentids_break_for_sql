# utils.py

import pandas as pd

def break_up_pidms(input_csv, output_txt):
    """
    Reads a CSV file containing PIDMs, formats them as 7-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    in the format "OR k.pidm IN (...)" and writes them to an output .txt file.

    :param input_csv: Path to the CSV file containing PIDMs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=None, names=['PIDM'])
    df['PIDM'] = df['PIDM'].astype(str).str.zfill(7)

    pidm_groups = [df['PIDM'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []
    
    for group in pidm_groups:
        if len(group) > 1:
            formatted_pidms = [f"'{pidm}'" for pidm in group[:-1]] + [group[-1]]
        else:
            formatted_pidms = [group[0]]
        
        sql_query = f"OR k.pidm IN ({', '.join(formatted_pidms)})"
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))
    
    print(f"SQL statements saved to {output_txt}")


def break_up_whkeys(input_csv, output_txt):
    """
    Reads a CSV file containing WHKEYs, formats them as 9-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    in the format "OR k.whkey IN (...)" and writes them to an output .txt file.

    :param input_csv: Path to the CSV file containing WHKEYs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=None, names=['WHKEY'])
    df['WHKEY'] = df['WHKEY'].astype(str).str.zfill(9)

    whkey_groups = [df['WHKEY'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []
    
    for group in whkey_groups:
        if len(group) > 1:
            formatted_whkeys = [f"'{whkey}'" for whkey in group[:-1]] + [group[-1]]
        else:
            formatted_whkeys = [group[0]]
        
        sql_query = f"OR k.whkey IN ({', '.join(formatted_whkeys)})"
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))
    
    print(f"SQL statements saved to {output_txt}")


def break_up_pantherids(input_csv, output_txt):
    """
    Reads a CSV file containing PantherIDs, formats them as 9-digit strings,
    and splits them into groups of 1000. Generates SQL statements
    in the format "OR k.pantherid IN (...)" and writes them to an output .txt file.

    :param input_csv: Path to the CSV file containing PantherIDs.
    :param output_txt: Path to the output text file where the queries will be saved.
    """
    df = pd.read_csv(input_csv, header=None, names=['PANTHERID'])
    df['PANTHERID'] = df['PANTHERID'].astype(str).str.zfill(9)

    pantherid_groups = [df['PANTHERID'][i:i+1000].tolist() for i in range(0, len(df), 1000)]
    
    sql_queries = []
    
    for group in pantherid_groups:
        if len(group) > 1:
            formatted_pantherids = [f"'{pantherid}'" for pantherid in group[:-1]] + [group[-1]]
        else:
            formatted_pantherids = [group[0]]
        
        sql_query = f"OR k.pantherid IN ({', '.join(formatted_pantherids)})"
        sql_queries.append(sql_query)
    
    with open(output_txt, 'w') as f:
        f.write("\n".join(sql_queries))
    
    print(f"SQL statements saved to {output_txt}")
