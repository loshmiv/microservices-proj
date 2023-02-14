import React, { useState, useEffect, PropsWithRef } from 'react';
import Wrapper from './Wrapper';
import { redirect } from 'react-router-dom';
import { Product } from '../interfaces/product';
import { useParams } from 'react-router-dom';


const ProductsEdit = (props: PropsWithRef<any>) => {
  const [title, setTitle] = useState('');
  const [image, setImage] = useState('');
  const [redir, setRedirect] = useState(false);

  let { id } = useParams();

  useEffect(() => {
    (
      async () => {
        const response = await fetch(`http://localhost:8000/api/products/${id}`);

        const product: Product = await response.json();

        setTitle(product.title);
        setImage(product.image);
      }
    )();
  }, []);

  const submit = async (e) => {
    e.preventDefault();
    
    await fetch(`http://localhost:8000/api/products/${id}`, {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        title,
        image
      })
    });

    setRedirect(true);
  }

  if (redir) {
    return redirect('/admin/products');
  } 

  return (
    <Wrapper>
      <form onSubmit={submit}>
        <div className="form-group">
          <label>Title</label>
          <input type="next" className="form-control" name="title" 
            defaultValue={title}
            onChange={e => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Image</label>
          <input type="text" className="form-control" name="image"
            defaultValue={image}
            onChange={e => setImage(e.target.value)}
          />
        </div>
        <button className="btn btn-outline-scondary">Save</button>
      </form>
    </Wrapper>

  );
};


export default ProductsEdit;
