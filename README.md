# Task_API_01


Hi Everyone 🙂 
Below you can find the FastAPI exercise. Let me know if you need any help or resources.
Goodluck! 

Fast API - framework for creating RESTful APIs for web applications. It allows defining RESTful endpoints. 

Make sure you know the definitions, and have a good high level understanding of:
•	REST API
•	REST methods: GET, POST, PUT, PATCH, DELETE
•	API endpoint
•	JSON formats (key-value pairs) and CSV formats (tabular data)

Task:
Using Python and the built-in libraries csv, json, and the external library fastAPI (requires installation), create a REST API with an endpoint /csv_to_json using the POST method, where you can send data in CSV format with named columns and with an arbitrary number of columns and rows. 

The endpoint should read the CSV file, and use it create and return a JSON file.

After processing, each column name from the CSV file should become a key name in the JSON file, 
and the rows in that column should be collected into a list and assigned to the key.

Example input output:
input CSV:
```
column_name_1, column_name_2, column_name_3
row_0_col_1, row_0_col_2, row_0_col_3
row_1_col_1, row_1_col_2, row_1_col_3
row_2_col_1, row_2_col_2, row_2_col_3
```

output JSON:
```
[
    {
        "column_name_1": ["row_0_col_1", "row_1_col_1", "row_2_col_1"],
        "column_name_2": ["row_0_col_2", "row_1_col_2", "row_2_col_2"],
        "column_name_3": ["row_0_col_3", "row_1_col_3", "row_2_col_3"]
    }
]
