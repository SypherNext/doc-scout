# Step 056: File Handling: Common Mistakes

- **Large datasets (10GB+):** Reading the entire file into memory with `read()` or `readlines()` will crash your program. Use incremental reading (line-by-line iteration) or libraries like `pandas.read_csv(chunksize=...)`.

Files in this step:
- `mistake_1_forgetting_to_close_a_file.py`
- `mistake_1_forgetting_to_close_a_file_2.py`
- `mistake_2_writing_in_w_mode_when_you_meant_a_or_x_3.py`
- `mistake_2_writing_in_w_mode_when_you_meant_a_or_x_4.py`
- `mistake_3_not_specifying_encoding_5.py`
- `mistake_3_not_specifying_encoding_6.py`
- `mistake_4_using_read_on_an_entire_large_file_7.py`
- `mistake_4_using_read_on_an_entire_large_file_8.py`
- `mistake_4_using_read_on_an_entire_large_file_9.py`
- `mistake_5_using_string_methods_for_path_joining_10.py`
- `mistake_5_using_string_methods_for_path_joining_11.py`

This step also carries forward `data/sample_docs/`, the shared seed document collection this course builds its file-handling and chunking examples on, and that later courses in this path ingest.
