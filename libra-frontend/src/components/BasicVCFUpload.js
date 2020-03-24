import React from 'react';
import axios from 'axios';

class BasicVCFUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {

    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('project_id', this.props.project_id);
    // data.append('filename', this.fileName.value);

    // axios.post('http://localhost:5000/upload',{
    //   file: this.uploadInput.files[0],
    //   filename: this.fileName.value
    // },{headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
    //   .then(res => {
    //     res.json().then((body) => {
    //     this.setState({ imageURL: `http://localhost:5000/${body.file}` });
    //   });
    //   })
    //   .catch(err =>  {
    //     if(err.response) {
    //       console.log(axios.defaults.headers.common)
    //       console.log(err.response.data)
    //       if(err.response.status == 401) {
    //         this.props.history.push('/');
    //       }
    //     }
    //   });
    fetch('http://localhost:5000/vcf_upload', {
      method: 'POST',
      body: data,
      headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
      // 'Content-Type': 'application/x-www-form-urlencoded',
    }
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL: `http://localhost:5000/${body.file}` });
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" accept=".gz, .vcf" />
        </div>
        <div>
          <button>Upload VCF to database</button>
        </div>
      </form>
    );
  }
}

export default BasicVCFUpload;