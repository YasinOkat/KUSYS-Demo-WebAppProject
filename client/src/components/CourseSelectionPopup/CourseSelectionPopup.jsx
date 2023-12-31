import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { MDBCheckbox, MDBBtn } from 'mdb-react-ui-kit';

const CourseSelectionPopup = ({ student, onClose, updateStudentList, authToken, setStudents }) => {
    const [availableCourses, setAvailableCourses] = useState([]);
    const [selectedCourseIds, setSelectedCourseIds] = useState([]);


    // When the popup opens, send request to the API and fetch the courses
    useEffect(() => {
        axios.get(`http://localhost:5000/courses`)
            .then(response => {
                setAvailableCourses(response.data);
            })
            .catch(error => {
                console.error('Error fetching available courses:', error);
            });
    }, [student.student_id]);

    const handleCourseChange = event => {
        const courseId = event.target.value;
        if (selectedCourseIds.includes(courseId)) {
            setSelectedCourseIds(prevIds => prevIds.filter(id => id !== courseId));
        } else {
            setSelectedCourseIds(prevIds => [...prevIds, courseId]);
        }
    };

    // After selecting courses, send a request to the API and update the courses
    const handleSubmit = event => {
        event.preventDefault();
        const token = localStorage.getItem('authToken'); // Since the endpoint requires login_required, we are sending the token
        const userRole = localStorage.getItem('userRole'); // Only update if the user is admin
        
        axios.post(
            `http://localhost:5000/select_courses/${student.student_id}`,
            { selected_courses: selectedCourseIds, userRole },
            {
                headers: {
                    Authorization: `Bearer ${token}`, // Sending the JWT token
                },
            }
        )
        .then(response => {
            onClose();
            updateStudentList(authToken, setStudents); // After closing the popup, automatically update the studends list
        })
        .catch(error => {
            console.error('Error selecting courses:', error);
        });
    };

    const handleCancel = () => {
        onClose();
    };

    return (
        <div className="popup">
            <div className="popup-content">
                <h2>Select Courses for {student.first_name} {student.last_name}</h2>
                <form onSubmit={handleSubmit}>
                    {availableCourses.map(course => (
                        <div key={course.course_id}>
                            <label>
                                <MDBCheckbox
                                    type="checkbox"
                                    label={course.course_name}
                                    name="selected_courses[]"
                                    value={course.course_id}
                                    checked={selectedCourseIds.includes(course.course_id)}
                                    onChange={handleCourseChange}
                                />
                            </label>
                        </div>
                    ))}
                    <div className="button-container">
                        <MDBBtn type="submit" className="button-margin">Save</MDBBtn>
                        <MDBBtn type="button" onClick={handleCancel} className="cancel-button-custom">Cancel</MDBBtn>
                    </div>
                    
                </form>
            </div>
        </div>
    );
};

export default CourseSelectionPopup;
