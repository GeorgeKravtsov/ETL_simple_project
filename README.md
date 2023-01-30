# Description of ETL Simple Project
# Necessary:
# - using the MySQL database (or another relational database, for example, PostgreSQL), create a data schema corresponding to the given files (many-to-one relationship);
# - write a script  which load these two files and write data to the database.
# Compose database queries to return:
# - list of rooms and the number of students in each of them;
# - top 5 rooms with the smallest average age of students;
# - top 5 rooms with the biggest difference in student age;
# - list of rooms where students of different sexes live.
# Requirements and remarks:
# - offer options for optimizing queries using indexes;
# - as a result, you need to generate an SQL query that will add the necessary indexes
# upload result in JSON or XML format;
# - all "mathematics" should be done at the database level.
# The command interface must support the following input parameters:
# - students (path to student file);
# - rooms (path to room file);
# - format (output format: xml or json);
# - use OOP and SOLID;
# - no use of ORM (use SQL).
