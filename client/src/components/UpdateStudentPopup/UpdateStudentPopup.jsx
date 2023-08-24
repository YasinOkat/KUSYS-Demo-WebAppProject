import React, { useState } from 'react';
import axios from 'axios';
import { MDBInput, MDBBtn, MDBCheckbox } from 'mdb-react-ui-kit';
import './UpdateStudentPopup.css';

const UpdateStudentPopup = ({ student, onClose, updateStudentList, setStudents  }) => {
    
    const authToken = localStorage.getItem('authToken');
    
    const [formData, setFormData] = useState({
        first_name: student.first_name,
        last_name: student.last_name,
        birth_date: student.birth_date,
        username: student.username,
        isAdmin: student.role === 'admin',
    });


    const [isFieldsEmpty, setIsFieldsEmpty] = useState(false);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setFormData(prevData => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleCheckboxChange = event => {
        const { name, checked } = event.target;
        setFormData(prevData => ({
            ...prevData,
            [name]: checked,
        }));
    };

    const handleSubmit = event => {
        event.preventDefault();

        if (!formData.first_name || !formData.last_name || !formData.birth_date || !formData.username) {
            setIsFieldsEmpty(true);
            return;
        }

        setIsFieldsEmpty(false);

        axios.post(`http://localhost:5000/update_student/${student.student_id}`, formData, {
            headers: {
                Authorization: `Bearer ${authToken}`,
            }
        })
            .then(response => {
                console.log('Student updated successfully');
                onClose();
                updateStudentList(authToken, setStudents);
            })
            .catch(error => {
                console.error('Error updating student:', error);
            });
    };
    

    const handleCancel = () => {
        onClose();
    };

    return (
        <div className="popup">
            <div className="popup-content">
                <h2>Update Student</h2>
                <form onSubmit={handleSubmit}>
                    <MDBInput
                            label="First Name"
                            type="text"
                            wrapperClass='mb-4 w-100'
                            name="first_name"
                            value={formData.first_name}
                            onChange={handleInputChange}
                            className="input-margin"
                    />
                    <MDBInput
                        label="Last Name"
                        type="text"
                        name="last_name"
                        wrapperClass='mb-4 w-100'
                        value={formData.last_name}
                        onChange={handleInputChange}
                        className="input-margin"
                    />
                    <MDBInput
                        label="Birth Day"
                        type="date"
                        name="birth_date"
                        wrapperClass='mb-4 w-100'
                        value={formData.birth_date}
                        onChange={handleInputChange}
                        className="input-margin"
                    />
                    <MDBInput
                        label="Username"
                        type="text"
                        name="username"
                        wrapperClass='mb-4 w-100'
                        value={formData.username}
                        onChange={handleInputChange}
                        className="input-margin"
                    />
                    <div className="error-container">
                        {isFieldsEmpty && (
                            <p className="error-message">Please fill in all fields</p>
                        )}
                    </div>
                    <MDBCheckbox
                        id="isAdmin"
                        name="isAdmin"
                        label="Admin"
                        checked={formData.isAdmin}
                        onChange={handleCheckboxChange}
                    />

                    <div className="button-container"></div>
                    <div className="button-container">
                        <MDBBtn type="submit" className="button-margin">Update</MDBBtn>
                        <MDBBtn type="button" onClick={handleCancel} className="cancel-button-custom">Cancel</MDBBtn>
                    </div>
                    
                </form>
            </div>
        </div>
    );
};

export default UpdateStudentPopup;
