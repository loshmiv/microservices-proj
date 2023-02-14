import React, { SyntheticEvent, useState } from 'react';
import Wrapper from './Wrapper';
import { redirect } from 'react-router-dom';


const ProductsCreate = () => {
  const [title, setTitle] = useState('');
  const [image, setImage] = useState('');
  const [redir, setRedirect] = useState(false);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();
    
    await fetch('http://localhost:8000/api/products', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        title,
        image
      })
    });

    setRedirect(true);
  }

  if (redir) {
    return redirect('/admin/products')
  } 

  return (
    <Wrapper>
      <form onSubmit={submit}>
        <div className="form-group">
          <label>Title</label>
          <input type="next" className="form-control" name="title" 
            onChange = {e => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Image</label>
          <input type="text" className="form-control" name="image"
            onChange = {e => setImage(e.target.value)}
          />
        </div>
        <button className="btn btn-outline-scondary">Save</button>
      </form>
    </Wrapper>

  );
};


export default ProductsCreate;
