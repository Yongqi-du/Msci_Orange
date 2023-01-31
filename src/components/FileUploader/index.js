import './style.css';

export const FileUploader = ({}) => {
    return (
        <form method="post" action="#" id="#">
            <div className="form-group files">
                <label>
                    Upload Your File
                <input type="file" className="form-control" multiple=""/>
                </label>
            </div>
            <button> Submit</button>
        </form>
    )
};