const express = require('express')
const app = express()
const port = 3000
const cors = require("cors")
const multer = require('multer');
const path = require("path")
const { spawn } = require('child_process');

app.use(cors())

let storedFilename;


const storage = multer.diskStorage({
    destination: './uploads/',
    filename: (req, file, cb) => {
        storedFilename = 'potholeToEdit' + path.extname(file.originalname);
        cb(null, storedFilename);
    }
});

// Initialize upload
const upload = multer({
    storage: storage,
    limits: { fileSize: 1000000 }, // Limit file size to 1MB
    fileFilter: (req, file, cb) => {
        checkFileType(file, cb);
    }
}).single('image');

// Check file type
function checkFileType(file, cb) {
    const filetypes = /jpeg|jpg|png|gif/;
    const extname = filetypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = filetypes.test(file.mimetype);

    if (mimetype && extname) {
        return cb(null, true);
    } else {
        cb('Error: Images Only!');
    }
}

app.post('/handleImage', (req, res) => {
    upload(req, res, (err) => {
        if (err) {
            res.status(400).send(err);
        } else {
            if (req.file == undefined) {
                res.status(400).send('No file selected!');
            }
        }
        console.log("FIleName: " + storedFilename)

        // Spawn a new process to run the Python script
        const pythonProcess = spawn('python', ['./scripts/testScripts.py', `./uploads/${storedFilename}`]);

        // Capture the output from the Python script
        pythonProcess.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
            res.send(data.toString());
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
            res.status(500).send(data.toString());
        });

        pythonProcess.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    })

})


app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})