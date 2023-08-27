# Write your MySQL query statement below
SELECT
    st.student_id,
    st.student_name,
    sub.subject_name,
    COUNT(exam.subject_name) as attended_exams
FROM 
    Students as st
CROSS JOIN
    Subjects as sub
LEFT JOIN 
    Examinations as exam on st.student_id = exam.student_id and sub.subject_name = exam.subject_name
GROUP BY
    sub.subject_name, st.student_id
ORDER BY
    st.student_id, sub.subject_name
