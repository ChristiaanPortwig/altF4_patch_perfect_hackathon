import React, { useState } from 'react'
import { Form } from 'react-router-dom';
import axios from 'axios';
import { data } from 'autoprefixer';

const Home = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [bagsNeeded, setBagsNeeded] = useState(null)


    let sendImage = () => {
        const formData = new FormData();
        formData.append('image', selectedFile);

        axios.post('http://localhost:3000/handleimage', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then((res) => {
                setBagsNeeded(res.data)
            })
            .catch((error) => {
                console.log("Error: " + error)
            })
    }

    let handleButtonClick = () => {
        document.getElementById("fileChooser").click()
    }

    let handleFileChange = (event) => {
        const file = event.target.files[0];
        setSelectedFile(file);

        // Create a preview URL for the selected image
        const reader = new FileReader();
        reader.onloadend = () => {
            setPreview(reader.result);
        };
        reader.readAsDataURL(file);
    }
    return (
        <div>
            <div className="card text-center border rounded bg-thistle min-h-screen w-75">
                <div className="card-header">
                    Alt + F4 Pothole Prediction Model
                </div>
                <h1 className='text-lg'>Pothole Repair Estimator</h1>
                <h3>Upload an image of the pothole and enter its dimensions to get the recommended amount of tar needed for repair.</h3>

                <div className="card-body d-flex justify-content-between">
                    <div>
                        <button onClick={handleButtonClick} className='w-[600px] p-3 border border-secondary mt-5'>
                            <h1>Select image</h1>
                            {preview ?
                                (<img src={preview} alt="Selected" className='mx-auto' />) :
                                (<img src={"potholePlaceholder.jpeg"} alt="Selected" className='mx-auto' />)
                            }
                        </button>
                        <input type="file" accept="image/*" onChange={handleFileChange} className='hidden' id='fileChooser' />
                        <button type="button" className="btn btn-primary w-[600px] block mx-auto my-1" onClick={sendImage}>convert</button>
                    </div>
                    <div>
                        <h1 className='my-auto'>Estimated use:</h1>
                        <h1 id="useAmount">{bagsNeeded}</h1>
                    </div>
                </div>

            </div>
        </div>
    )
}

export default Home