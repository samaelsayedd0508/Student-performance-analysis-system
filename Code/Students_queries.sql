SELECT 
    s.Subject_name,
    st.Student_name,
    a1.Score,
    a1.Performance_Grade
FROM Assessment a1
JOIN Student st ON a1.Student_ID = st.Student_ID
JOIN Subject s ON a1.Subject_ID = s.Subject_ID
WHERE a1.Score = (
    SELECT MAX(a2.Score)
    FROM Assessment a2
    WHERE a2.Subject_ID = a1.Subject_ID
)
ORDER BY s.Subject_name;




SELECT 
    s.Subject_name,
    SUM(a.Attendance IN ('Present', 'Late')) AS Present_Count,
    SUM(a.Attendance IN ('Absent', 'Excused')) AS Absent_Count,
    ROUND(100.0 * SUM(a.Attendance IN ('Present', 'Late')) / COUNT(*), 2) AS Attendance_Rate
FROM Assessment a
JOIN Subject s ON a.Subject_ID = s.Subject_ID
GROUP BY s.Subject_name
ORDER BY Attendance_Rate DESC;




SELECT s.subject_name ,
round(avg(a.score),2) as AveragePerSubject
from Assessment as a
join Subject s on a.Subject_ID = s.Subject_ID
GROUP by subject_name
order by AveragePerSubject



