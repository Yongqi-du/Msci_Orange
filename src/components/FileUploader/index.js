import './style.css';

// export const FileUploader = ({}) => {
//     return (
//         <form method="post" action="#" id="#">
//             <div className="form-group files">
//                 <label>
//                     Upload Your File
//                 <input type="file" className="form-control" multiple=""/>
//                 </label>
//             </div>
//             <button> Submit</button>
//         </form>
//     )
// };

import React , {useState} from 'react';
import { uploadFile } from 'react-s3';


const S3_BUCKET ='rbkhousingbucket';
const REGION ='eu-west-2';
const ACCESS_KEY ='AKIAX25LW44KLU6GEL7K';
const SECRET_ACCESS_KEY ='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';

const config = {
    bucketName: S3_BUCKET,
    region: REGION,
    accessKeyId: ACCESS_KEY,
    secretAccessKey: SECRET_ACCESS_KEY,
}

export const FileUploader = () => {

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileInput = (e) => {
        setSelectedFile(e.target.files[0]);
    }

    const handleUpload = async (file) => {
        uploadFile(file, config)
            .then(data => console.log(data))
            .catch(err => console.error(err))
    }

    return <div>
        <div>Data Sheet</div>
        <input type="file" onChange={handleFileInput}/>
        <button onClick={() => handleUpload(selectedFile)}>Upload File</button>
    </div>
}

// export default FileUploader;