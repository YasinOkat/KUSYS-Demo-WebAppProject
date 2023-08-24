// studentService.js

import axios from 'axios';

const updateStudentList = (authToken, setStudents) => {
    axios.get('http://localhost:5000/students', {
        headers: {
            Authorization: `Bearer ${authToken}`,
        }
    })
    .then(response => {
        // Fetch student details for each student
        const studentsWithDetails = response.data.students.map(async student => {
            try {
                const detailsResponse = await axios.get(`http://localhost:5000/student_details/${student.student_id}`, {
                    headers: {
                        Authorization: `Bearer ${authToken}`,
                    }
                });
                return { ...student, details: detailsResponse.data };
            } catch (detailsError) {
                console.error('Error fetching student details:', detailsError);
                return { ...student, details: null };
            }
        });

        // Wait for all details requests to complete and then update the state
        Promise.all(studentsWithDetails).then(updatedStudents => {
            setStudents(updatedStudents); // Update the students state
        });
    })
    .catch(error => {
        console.error('Error fetching students:', error);
    });
};

const deleteStudent = (student, authToken, setStudents, setSelectedStudent, userRole) => {
    if (!student) {
        console.error('Selected student is null, cannot delete.');
        return;
    }

    if (window.confirm(`Are you sure you want to delete ${student.first_name} ${student.last_name}?`)) {
        axios.post(`http://localhost:5000/delete_student/${student.student_id}`, { userRole }, {
            headers: {
                Authorization: `Bearer ${authToken}`,
            }
        })
        .then(response => {
            console.log('Student deleted successfully');
            updateStudentList(authToken, setStudents);
        })
        .catch(error => {
            console.error('Error deleting student:', error);
        });
    }
};
export { updateStudentList, deleteStudent };