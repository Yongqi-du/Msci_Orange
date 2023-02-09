import './style.css';
import {read, utils, writeFile} from 'xlsx';
import * as XLSX from 'xlsx'
const readUploadFile = (e) => {
    e.preventDefault();
    if (e.target.files) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const data = e.target.result;
            const workbook = XLSX.read(data, {type: "array"});
            const sheetName = workbook.SheetNames[0];
            const worksheet = workbook.Sheets[sheetName];
            const json = XLSX.utils.sheet_to_json(worksheet);
            console.log(json);
        };
       reader.readAsArrayBuffer(e.target.files[0]);
    }
}

export const FileUploader = ({}) => {
    return (
        <form method="post" action="#" id="#">
            <div className="form-group files">
                <label>
                    Upload Your File
                <input id="inp" type="file" className="form-control" multiple="" onChange={readUploadFile}/>
                </label>
            </div>
            <button> Submit</button>
        </form>
    )
};