import pandas as pd

# -------------------------------
# Task 1: Data Preparation
# -------------------------------
students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None,
              'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}

enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python', 'Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
}

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}

students = pd.DataFrame(students_data)
enrollments = pd.DataFrame(enrollments_data)
scores = pd.DataFrame(scores_data)

print("=== TASK 1: Data Preparation ===")
print("\nOriginal Students DataFrame:\n", students)

# Null value analysis
print("\nNull Value Analysis:")
for col in students.columns:
    nulls = students[col].isnull().sum()
    perc = (nulls / len(students)) * 100
    print(f"Column: {col}, Nulls: {nulls} ({perc:.2f}%)")

# Fill missing city with 'Unknown'
students['city'] = students['city'].fillna('Unknown')

# Drop rows where name is missing
students = students.dropna(subset=['name'])

print("\nCleaned Students DataFrame:\n", students)

# -------------------------------
# Task 2: Join Operations
# -------------------------------
print("\n=== TASK 2: Join Operations ===")

# Inner Join
inner_join = pd.merge(students, enrollments, on='student_id', how='inner')
print("\nInner Join Result:\n", inner_join)
print("Number of students in result:", len(inner_join))
excluded = set(students['student_id']) - set(inner_join['student_id'])
print("Excluded students:", excluded, "- Not in enrollments table")

# Left Join
left_join = pd.merge(students, enrollments, on='student_id', how='left')
print("\nLeft Join Result:\n", left_join)
print("Total rows:", len(left_join))
null_courses = left_join[left_join['course_name'].isnull()]['student_id'].tolist()
print("Students with null course_name:", null_courses)

# Right Join
right_join = pd.merge(students, enrollments, on='student_id', how='right')
print("\nRight Join Result:\n", right_join)
print("Total rows:", len(right_join))
missing_names = right_join[right_join['name'].isnull()]['student_id'].tolist()
print("Student_ids without names:", missing_names)

# Full Outer Join
outer_join = pd.merge(students, enrollments, on='student_id', how='outer', indicator=True)
print("\nFull Outer Join Result:\n", outer_join)
print("Total rows:", len(outer_join))
print("Rows with null name OR null course_name:\n", outer_join[outer_join['name'].isnull() | outer_join['course_name'].isnull()])
print("Merge source distribution:\n", outer_join['_merge'].value_counts())

# -------------------------------
# Task 3: Lookup and Automation
# -------------------------------
print("\n=== TASK 3: Lookup and Automation ===")

# Lookup Operation
score_map = dict(zip(scores['student_id'], scores['exam_score']))
students['exam_score'] = students['student_id'].map(score_map)
print("\nLookup Operation Result:\n", students[['student_id', 'name', 'exam_score']])

# Merge Operation (drop exam_score before merge to avoid duplicate column names)
merge_scores = pd.merge(students.drop(columns=['exam_score']), scores, on='student_id', how='left')
print("\nMerge Operation Result:\n", merge_scores[['student_id', 'name', 'exam_score']])

print("\nExplanation: .map() is more efficient for simple key-value lookups "
      "because it directly applies a dictionary mapping. pd.merge() is more "
      "powerful for complex joins but involves more overhead.")

# Automation Function
def auto_merge(df1, df2, join_type, key_column):
    merged = pd.merge(df1, df2, on=key_column, how=join_type)
    return {
        'result_df': merged,
        'row_count': len(merged),
        'join_type': join_type
    }

# Test function
test_inner = auto_merge(students, enrollments, 'inner', 'student_id')
test_left = auto_merge(students, enrollments, 'left', 'student_id')

print("\nAutomation Function Test:")
print("Join Type:", test_inner['join_type'])
print("Rows in Result:", test_inner['row_count'])
print("Result Preview:\n", test_inner['result_df'].head())

print("\nJoin Type:", test_left['join_type'])
print("Rows in Result:", test_left['row_count'])
print("Result Preview:\n", test_left['result_df'].head())
