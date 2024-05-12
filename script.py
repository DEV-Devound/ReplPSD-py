const { PhotoshopAPI } = require('@adobe/aio-lib-photoshop-api');
const fs = require('fs');
const express = require('express');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/write', upload.fields([{ name: 'psd_file' }, { name: 'profile_image' }]), async (req, res) => {
    const firstName = req.body.first_name;
    const lastName = req.body.last_name;
    const psdFile = req.files.psd_file[0].path;
    const profileImage = req.files.profile_image[0].path;

    const client = await sdk.init('<ims org id>', '<api key>', '<valid auth token>');

    // Load the PSD file
    const document = await client.open(psdFile);

    // Edit the text layers
    const firstNameLayer = document.layers.find(layer => layer.name === 'first_name');
    const lastNameLayer = document.layers.find(layer => layer.name === 'last_name');
    firstNameLayer.text = firstName;
    lastNameLayer.text = lastName;

    // Create a smart object with the profile image
    const smartObject = await client.createSmartObject(profileImage);
    smartObject.name = 'profile_image';
    smartObject.applyLayerEffects({ dropShadow: true, innerShadow: true, outerGlow: true, innerGlow: true });

    // Add the smart object to the document
    document.layers.push(smartObject);

    // Save the document as a new PSD file
    const newPsdFile = 'new_' + psdFile;
    await client.saveAs(newPsdFile, document);

    res.send('File has been written with the name ' + newPsdFile);
});

app.listen(3000, () => console.log('Server started on port 3000'));