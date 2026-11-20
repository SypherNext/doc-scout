# Step 016: Variables: Common Mistakes

Dynamic typing is a feature of Python, but that does not mean you should change a variable's type mid-function. Code that does this is harder to read, harder to debug, and more likely to hide bugs. Exceptions exist (the `process_prediction` function in Build It deliberately handles multiple input types at a boundary) but inside your logic, keep each variable's type stable.

Files in this step:
- `mistake_1_using_an_unassigned_variable.py`
- `mistake_1_using_an_unassigned_variable_2.py`
- `mistake_3_accidentally_shadowing_a_built_in_3.py`
