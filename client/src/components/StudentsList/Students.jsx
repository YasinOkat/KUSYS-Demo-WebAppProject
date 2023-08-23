import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import './Students.css'; // Import the CSS file for styling
import UpdateStudentPopup from '../UpdateStudentPopup/UpdateStudentPopup';
import CreateStudentPopup from '../CreateStudentPopup/CreateStudentPopup';
import CourseSelectionPopup from '../CourseSelectionPopup/CourseSelectionPopup';
import DeleteIcon from '@mui/icons-material/Delete';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import { MDBBtn } from 'mdb-react-ui-kit';
import InfoIcon from '@mui/icons-material/Info';
import EditNoteIcon from '@mui/icons-material/EditNote';
import AssignmentIcon from '@mui/icons-material/Assignment';
import AddBoxIcon from '@mui/icons-material/AddBox'
import { updateStudentList, deleteStudent } from '../../utils';


const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [selectedStudent, setSelectedStudent] = useState(null);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [studentDetails, setStudentDetails] = useState(null);
    const [isUpdatePopupOpen, setIsUpdatePopupOpen] = useState(false);
    const [isCreatePopupOpen, setIsCreatePopupOpen] = useState(false);
    const [isCourseSelectionPopupOpen, setIsCourseSelectionPopupOpen] = useState(false);
    const [userRole, setUserRole] = useState('');
    const [userId, setUserId] = useState(''); // Add this state variable for the user's ID
    const history = useHistory();
    const authToken = localStorage.getItem('authToken');

    useEffect(() => {
        
        const userId = localStorage.getItem('userId');
        setUserId(parseInt(userId)); 
        
        axios.get('http://localhost:5000/check_role', {
          headers: {
            Authorization: `Bearer ${authToken}`,
          }
        })
        .then(response => {
            setUserRole(response.data.role);
            updateStudentList(authToken, setStudents);
        })
        .catch(error => {
          console.error(error);
        });
      }, []);

    const openUpdatePopup = student => {
        setSelectedStudent(student);
        setIsUpdatePopupOpen(true);
    };

    const openCreatePopup = () => {
        setIsCreatePopupOpen(true);
    };

    const openCourseSelectionPopup = student => {
        setSelectedStudent(student);
        setIsCourseSelectionPopupOpen(true);
    };

    const handleDeleteStudent = student => {
        deleteStudent(student, authToken, setStudents, setSelectedStudent, userRole);
    };

    const openPopup = student => {
        setSelectedStudent(student);

        axios.get(`http://localhost:5000/student_details/${student.student_id}`, {
            headers: {
                Authorization: `Bearer ${authToken}`,
            }
        })
        .then(response => {
            setStudentDetails(response.data);
            setIsPopupOpen(true);
            console.log('API Response:', response.data);
        })
        .catch(error => {
            console.error('Error fetching student details:', error);
        });
    };

    const closePopup = () => {
        setSelectedStudent(null);
        setIsPopupOpen(false);
    };
    

    const handleLogout = () => {
        axios.get('http://localhost:5000/logout')
            .then(response => {
                // Perform any client-side actions after logout (e.g., clear local storage)
                localStorage.removeItem('authToken');
                localStorage.removeItem('userId');
                localStorage.removeItem('userRole');
                history.push('/'); 
            })
            .catch(error => {
                console.error('Logout error:', error);
            });
    };
    
    return (
        
        <div className="student-list-container">
            <div className="top-right">
                <button className="logout-button" onClick={handleLogout}>Logout</button>
            </div>

            {userRole === 'admin' ? (
                <AddBoxIcon
                    className="create-button"
                    onClick={openCreatePopup}
                />
            ) : (
                <div className="empty-space"></div>
            )}

        <div className="student-list-wrapper">
            <ul className="student-list">
                {students.map(student => (
                    <li className="student-item" key={student.student_id}>
                        <div className="student-details">
                        <span className="student-name">
                            {student.first_name} {student.last_name}
                        </span>
                        {/* Display courses below the student's name */}
                        {(userRole === 'admin' || student.student_id === userId) && student.details ? (
                            <div className="course-list">
                                Courses: {student.details.courses.map((course, index) => (
                                    <span key={course.course_id}>
                                        {course.course_name}{index !== student.details.courses.length - 1 ? ', ' : ''}
                                    </span>
                                ))}
                                
                            </div>
                        ) : (
                            <p></p>
                        )}

                    </div>
                <div className="student-actions">
                    
                    {userRole === 'admin' || student.student_id === userId ? (
                      <AssignmentIcon
                        className="select-courses-button"
                        onClick={() => openCourseSelectionPopup(student)}
                      />
                    ) : null}
                    {userRole === 'admin' ? (
                      <EditNoteIcon
                        className="update-button"
                        onClick={() => openUpdatePopup(student)}
                      />
                    ) : null}
                    <InfoIcon
                      className="details-button"
                      onClick={() => openPopup(student)}
                      />
                    {userRole === 'admin' ? (
                      <DeleteIcon
                      className="delete-button"
                      onClick={() => handleDeleteStudent(student)}

                      />
                    ) : null}
                    
                  </div>
              </li>
            ))}
                {isUpdatePopupOpen && (
                    <UpdateStudentPopup
                        student={selectedStudent}
                        onClose={() => setIsUpdatePopupOpen(false)}
                        updateStudentList={updateStudentList}
                        
                    />
                )}
                {isCreatePopupOpen && (
                    <CreateStudentPopup
                        onClose={() => setIsCreatePopupOpen(false)}
                        updateStudentList={updateStudentList} // Pass the callback function
                    />
                )}

                {isCourseSelectionPopupOpen && (
                    <CourseSelectionPopup
                        student={selectedStudent}
                        onClose={() => setIsCourseSelectionPopupOpen(false)}
                        updateStudentList={updateStudentList}
                    />
                )}

                {isPopupOpen && (
                    <div className="popup">
                        {/* ... (student details popup content) */}
                    </div>
                )}
            </ul>
            {isPopupOpen && (
                <div className="popup">
                    <div className="popup-content">
                        {studentDetails ? (
                            <div>
                            <h2 className="popup-title">Details</h2>
                            <div className="student-info">
                                <p><strong>First Name:</strong> {studentDetails.first_name}</p>
                                <p><strong>Last Name:</strong> {studentDetails.last_name}</p>
                                <p><strong>Birth Date:</strong> {studentDetails.birth_date}</p>
                            </div>
                            
                            {(userRole === 'admin' || selectedStudent.student_id === userId) && selectedStudent.details ? (
                                <div className="course-list2">
                                    <strong>Courses:</strong> {selectedStudent.details.courses.map((course, index) => (
                                        <span key={course.course_id}>
                                            {course.course_name}{index !== selectedStudent.details.courses.length - 1 ? ', ' : ''}
                                        </span>
                                    ))}
                                </div>
                            ) : (
                                <p></p>
                            )}

                        </div>
                        
                        ) : (
                            <p>Loading student details...</p>
                        )}
                        <MDBBtn type="button" onClick={closePopup} className="cancel-button-custom1">Close</MDBBtn>
                    </div>
                </div>
            
            
            )}
        </div></div>
    );
};

export default StudentList;
