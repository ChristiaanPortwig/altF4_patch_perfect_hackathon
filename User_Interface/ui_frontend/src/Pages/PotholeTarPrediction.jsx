import React, { useState } from 'react';
//import 'bootstrap/dist/css/bootstrap.min.css';

const PotholeTarEstimator = () => {
    const [image, setImage] = useState(null);
    const [tarAmount, setTarAmount] = useState('');


    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        setImage(URL.createObjectURL(file));
        // Here you would typically send the image to your AI model for prediction
        // For demonstration, we'll just set a dummy tar amount
        setTarAmount('Estimated tar needed: 5 kg');
    };

    return (
        <div className="container my-5">
            <div className="card text-center" style={{ backgroundColor: '#e0f7fa', borderColor: '#00796b' }}>
                <div className="card-header" style={{ backgroundColor: '#00796b', color: '#ffffff' }}>
                    Pothole Tar Estimator
                </div>
                <div className="card-body">
                    <h5 className="card-title">Upload an image of the pothole</h5>
                    <input type="file" className="form-control-file mb-3" onChange={handleImageUpload} />
                    {image && <img src={image} alt="Pothole" className="img-fluid mb-3" />}
                    {tarAmount && <p className="card-text" style={{ color: '#004d40' }}>{tarAmount}</p>}
                </div>
            </div>
        </div>
    );
};

export default PotholeTarEstimator;
