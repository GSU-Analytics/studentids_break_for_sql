# **Automated SQL PIDM and WHKEY Search Breakups**

## **Purpose**
SQL has a built-in limit that prevents more than 1,000 values in a `WHERE student_id IN (...)` clause. This workspace provides a **Python script** that automates breaking up large lists of **PIDM, WHKEY, or PantherID** values into properly formatted SQL queries.

With this tool, you can **input a CSV or Excel file** containing student IDs, specify the ID type, and generate a `.txt` file containing multiple SQL-ready `IN` clauses, making it easy to copy and paste directly into your SQL queries.

---

## Project Structure

```plaintext
your_project/
│── uploads/        # Place your input CSV/XLSX files here
│── outputs/        # Processed output files will be stored here (auto-created)
│── scripts/        # Contains the main scripts
│   ├── main.py     # CLI script for processing files
│   ├── utils.py    # Utility functions for formatting IDs
│── README.md       # Instructions on how to use this workspace
│── environment.yaml # Conda environment configuration
```
## **Installation Instructions**

To set up the required dependencies, use the `id_sql_prep.yaml` file with Conda:

```bash
conda env create -f id_sql_prep.yaml
```

Once created, activate the environment:

```bash
conda activate id_sql_prep
```

---

## **Usage**

Run the script from the command line, specifying the input file and ID type.
Make sure that your Excel file or csv file is properly formatted (Single Column with a header formatted as: **PIDM, WHKEY, and pantherid**).

```bash
python scripts/main.py --file sample.csv --idtype whkey
python scripts/main.py --file sample.xlsx --idtype pidm
python scripts/main.py --file sample.csv --idtype pantherid
```

The script will output a `.txt` file in the `outputs/` directory, containing properly ending part of a `WHERE student_id IN (...)` broken into chunks of 1,000 IDs per `IN` clause.

---

## **Example**

If the input file contains the following WHKEYs:

```plaintext
123456
789012
345678
901234
... (more IDs)
```

The script will generate an output file (`outputs/query_WHKEY.txt`) containing:

```sql
OR k.whkey IN (
    '123456', '789012', '345678', '901234', ...
);
```

If the input file contains PantherIDs, the script ensures lowercase formatting:

```sql
OR k.whkey IN (
    'p12345', 'p67890', 'p24680', 'p13579', ...
);
```

For PIDMs:

```sql
OR k.pidm IN (
    '1000001', '1000002', '1000003', ...
);
```

The script automatically handles formatting and ensures each query block contains no more than 1,000 IDs.

If you need to reformat to match your overall query, then please do so in the query or outputted .txt file!

---

This tool simplifies SQL query preparation when working with large lists of student IDs, saving time and reducing manual errors.

