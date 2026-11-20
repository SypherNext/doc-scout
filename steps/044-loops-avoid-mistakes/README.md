# Step 044: Loops: Common Mistakes

- **NumPy/Pandas operations:** If you are looping over arrays to do arithmetic, use vectorised operations instead. `a + b` on numpy arrays is 10-100x faster than a loop.

Files in this step:
- `mistake_1_modifying_a_list_while_iterating_over_it.py`
- `mistake_1_modifying_a_list_while_iterating_over_it_2.py`
- `mistake_2_off_by_one_with_range_3.py`
- `mistake_3_forgetting_that_zip_stops_at_the_shortest_input_4.py`
- `mistake_3_forgetting_that_zip_stops_at_the_shortest_input_5.py`
- `mistake_4_infinite_while_loop_6.py`
- `mistake_4_infinite_while_loop_7.py`
- `mistake_5_using_append_in_a_loop_instead_of_a_comprehension_8.py`
- `mistake_5_using_append_in_a_loop_instead_of_a_comprehension_9.py`
